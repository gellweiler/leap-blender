""" Defines the how to move and rotate a object like a cube. """

from movable_blender_object import _MovableBlenderObject
from singleton import singleton
from workspace import Workspace
from mathutils import Vector
import bpy

@singleton
class BlenderObject(_MovableBlenderObject):
    
    def _rotate(self, axis, degree):
        """ Rotates object clockwise around axis by degree."""

        euler = bpy.context.scene.objects.active.rotation_euler
        if axis == 'x':
            euler.x += degree
        elif axis == 'y':
            euler.y += degree
        elif axis == 'z':
            euler.z += degree

    def _move(self, direction, value):
        """ Moves object into direction by value. """

        for view in Workspace().get3DView(): 
            offset = Vector((0.0, 0.0, 0.0))
            if direction == "horizontal":
                offset.x = value
            elif direction == "vertical":
                offset.y = value
            elif direction == "straightforward":
                offset.z = value

            bpy.context.scene.objects.active.location \
             = view.view_rotation*offset + bpy.context.scene.objects.active.location

    def rotate_vertical(self, degree):

        self._rotate("z", degree)

    def rotate_horizontal(self, degree):

        self._rotate("x", degree)

    def move_horizontal(self, value):

        self._move("horizontal", value)

    def move_vertical(self, value):

        self._move("vertical", value)

    def move_straightforward (self, value):

        self._move("straightforward", value)
