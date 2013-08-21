"""Defines the how to move and rotate the workspace (3D view)"""

from movable_blender_object import _MovableBlenderObject
from mathutils import Vector
from singleton import singleton
import bpy

@singleton
class Workspace(_MovableBlenderObject):
    """ Class for controlling the workspace. """

    def get3DView(self):
        """ Gets all current active 3D areas. """

        result = []
        for wm in bpy.data.window_managers:
            for w in wm.windows:
                for a in w.screen.areas:
                    for s in a.spaces:
                        if s.type == "VIEW_3D":
                            result.append(s.region_3d)
        return result

    def _move(self, direction, value):
        """ Moves view into direction by value. """

        for view in self.get3DView():
            offset = Vector((0.0, 0.0, 0.0))
            if direction == "horizontal":
                offset.x = value
            elif direction == "vertical":
                offset.y = value
            elif direction == "straightforward":
                offset.z = value

            view.view_location = view.view_rotation*offset + view.view_location

    def _rotate(self, axis, degree):
        """ Rotates view clockwise around axis by degree."""

        for view in self.get3DView():
            euler = view.view_rotation.to_euler()
            if axis == 'x':
                euler.x += degree
            elif axis == 'y':
                euler.y += degree
            elif axis == 'z':
                euler.z += degree
            view.view_rotation = euler.to_quaternion()


    def rotate_vertical(self, degree):
        """ Like pressing left or right on the numeric pad. """

        self._rotate("z", degree)


    def rotate_horizontal(self, degree):
        """ Like pressing up or down on the numeric pad. """

        self._rotate("x", degree)

    def zoom(self, value):
        """ Like moving the mouse wheel. """

        for view in self.get3DView():
            view.view_distance += value


    def move_horizontal(self, value):
        """ Like Shift+MMB and moving the mouse pointer horizontaly. 
            positive value to move left
            negative value to move right
        """
        
        self._move("horizontal", value)

    def move_vertical(self, value):
        """ Like Shift+MMB and moving the mouse pointer verticaly. 
            positive to move down
            negative to move up
        """
        
        self._move("vertical", value)

    def move_straightforward (self, value):

        self._move("straightforward", value)