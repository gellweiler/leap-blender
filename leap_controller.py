"""The main file which contains the hole logic"""
import bpy
import Leap
import time
import LeapPython
from functools import reduce
from mathutils import Vector
from bpy.props import BoolProperty, FloatProperty
from bpy.types import Operator
import workspace
import settings
import blender_object


class LeapController(bpy.types.Operator):
    bl_idname = "object.leap_blender"
    bl_label = "Leap Blender"
    bl_options = {'REGISTER', 'UNDO'}
    bl_property = "distance"
    activated = False
    frame = Leap.Frame()
    key_tap_timestamp = 0

    #GUI Check Box
    #activated = BoolProperty(
    #  name="Leap Controlled", 
    #  description="Enables controlling Object through Leap Motion", 
    #  default=False, 
    #  options={'ANIMATABLE'},
    #  subtype='NONE')

    distance = FloatProperty(  
       name="distance",  
       default=1.0,  
       subtype='DISTANCE',  
       unit='LENGTH',  
       description="distance"  
       ) 

    @classmethod  
    def poll(cls, context):  
        return True

    def modal(self, context, event):
        """ Listen for TIMER event and look for leap frames on every tick. """

        # Cancel LeapMotion control on pressing END key.
        if event.type == 'END':
            self.cancel(context)
            return

        if event.type == 'TIMER' and not self._updating:
            self._updating = True

            # Handle all new frames since last tick.
            last_frame = self.frame
            self.frame = self.controller.frame()
            #print (self.frame.id, last_frame.id) 
            if (
                (self.frame is not last_frame) and
                (self.frame.id > 0 and last_frame.id > 0)
            ):
                frames = []
                for i in range(0, self.frame.id - last_frame.id + 1):
                    if self.controller.frame(i).is_valid:
                        frames.append(self.controller.frame(i))
                self._process_frames(frames)

            self._updating = False
        return {'PASS_THROUGH'}

    def execute(self, context):
        dir = self.direction.normalized()  
        context.active_object.location += self.distance * dir
        return {'FINISHED'}

    def invoke(self, context, event):
        """ Invoke the leap device. """

        context.window_manager.modal_handler_add(self)
        self.controller = Leap.Controller()

        # Enable and improve KeyTab.
        self.controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        if (
            LeapPython.Config_set_float(self.controller.config, "Gesture.KeyTap.MinDownVelocity", settings.KeyTap_MinDownVelocity) and
            LeapPython.Config_set_float(self.controller.config, "Gesture.KeyTap.HistorySeconds", settings.KeyTap_HistorySeconds) and
            LeapPython.Config_set_float(self.controller.config, "Gesture.KeyTap.MindDistance", settings.KeyTap_MinDistance)
        ):
            self.controller.config.save()

        # Set timer to run every settings.framerate.
        context.window_manager.event_timer_add(settings.framerate, context.window)
        self._updating = False
        return {'RUNNING_MODAL'}

    def _process_frames(self, frames):
        """ Evaluate movements and moations in frame. """

        for g in frames[-1].gestures(frames[0]):
            if (g.type == Leap.Gesture.TYPE_KEY_TAP
                # See settings for explanation.
             and time.time() > (self.key_tap_timestamp + settings.key_tap_seconds_lock)):
                self.activated = not self.activated
                self.key_tap_timestamp = time.time()

        if self.activated:
            # Same control movements for workspace and blender objects,
            # except use one hand for controlling workspace and two for blender objects. 
            obj = None
            if len(frames[0].hands) > 1:
                obj1 = blender_object.BlenderObject()
                obj2 = workspace.Workspace()
            else:
                obj1 = workspace.Workspace()
                obj2 = blender_object.BlenderObject()

            #print(frames[0].hands.leftmost.palm_position)

            # Hand with fingers stretched.
            # Controls rotation and zooming.
            if len(frames[0].fingers) > 3 :
                v = self._frames_difference_vector(frames, lambda x: x.hands.leftmost.palm_position)
                # Zoom just applies for workspace.
                # Not all objects can zoom.
                print(v)
                zoom = getattr(obj1, "zoom", None)
                if zoom is not None:
                    obj1.zoom(v.z*settings.lb_factor)
                self._rotate(obj1, v)

            # Fist or hand without fingers.
            # Controls movements.
            elif len(frames[0].fingers) < 2 and len(frames[0].hands) > 0:
                v = self._frames_difference_vector(frames, lambda x: x.hands.leftmost.palm_position)
                print(v)
                self._move(obj2, v)
                

            #elif len(frames[0].fingers) < 2 and len(frames[0].hands) > 0:
            #    w = blender_object.BlenderObject()
            #    v = self._frames_difference_vector(frames, lambda x: x.hands[0].palm_position)
            #    self._move(o, v)
            #elif len(frames[0].fingers) == 1:
            #    o = workspace.Workspace()
            #    v = self._frames_difference_vector(frames, lambda x: x.hands[0].palm_position)
            #    self._move(o, v)

    def _frames_difference_vector(self, frames, attr_func):
        """ Calculates the difference Vector of attribute on the first and the last frame. """

        res = Vector((0.0, 0.0, 0.0))
        for i in (0, -1):
            #get attributes from frames[i]
            v = attr_func(frames[i])
            if i == 0:
                res.y -= v.y
                res.x -= v.x
                res.z -= v.z
            else:
                res.y += v.y
                res.x += v.x
                res.z += v.z

            if res.x > settings.max_x and res.x < -settings.max_x:
                res.y = 0
            if res.y > settings.max_y and res.y < -settings.max_y:
                res.y = 0
            if res.z > settings.max_z and res.z < -settings.max_z:
                res.z = 0
        return res

    def _move(self, obj, v):
        obj.move_horizontal(v.x*settings.lb_factor*(-1))
        obj.move_vertical(v.y*settings.lb_factor*(-1))
        obj.move_straightforward(v.z*settings.lb_factor*(-1))

    def _rotate(self, obj, v):
        obj.rotate_horizontal(v.y*settings.ld_factor*(-1))
        obj.rotate_vertical(v.x*settings.ld_factor)