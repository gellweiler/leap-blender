""" Initialises the Leap Blender Addon. """

import bpy
from . import leap_import
import Leap
import leap_controller
import leap_panel
import sys
from time import sleep
from mathutils import Vector
from bpy.types import Operator

bl_info = {
    'name': 'Leap Blender',
    'author': 'Jonas Pohlmann & Sebastian Gellweiler',
    'category' : '3D View',
}

def add_object_button(self, context):
    self.layout.operator(
    LeapController.bl_idname,
    text=LeapController.__doc__,
    icon='PLUGIN')

def register():
    bpy.utils.register_class(leap_controller.LeapController)
    bpy.utils.register_class(leap_panel.LeapPanel)
    bpy.types.VIEW3D_MT_object.append(add_object_button)
    print(sys.path)

def unregister():
    bpy.utils.unregister_class(leap_controller.LeapController)
    bpy.utils.unregister_class(leap_panel.LeapPanel)

if __name__ == "__main__":
    register()
