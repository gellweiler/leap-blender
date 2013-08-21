""""The interface for an object like a cube or the workspace"""
import bpy
class _MovableBlenderObject(object):
    """ Inteface for blender objects that can be moved and rotated. """


    def rotate_vertical(self, degree):
        raise NotImplemented

    def rotate_horizontal(self, degree):
        raise NotImplemented

    def move_horizontal(self, value):
        raise NotImplemented

    def move_vertical(self, value):
        raise NotImplemented

    def move_straightforward(self, value):
        raise NotImplemented