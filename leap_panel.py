""" Beta version of the panel which appears in Blender but does not contain any buttons. """
import bpy
from bpy.props import FloatProperty
from bpy.types import Operator  
import os

class LeapPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D" # window type panel is displayed in
    bl_region_type = "TOOLS" # region of window panel is displayed in
    bl_label = "Leap Motion Panel" # heading of panel

    def draw(self, context) :
        leap_panel_layout = self.layout.column(align = True)
        #leap_panel_layout.prop( context.scene, 'object.leap_blender' ) # draw input field for pyramide's height
        #leap_panel_layout.prop( context.scene, 'pyramide_width' ) # draw input field for pyramide's width
        #leap_panel_layout.operator("mesh.build_pyramide", text = "Build!") # draw Build! button
        #leap_panel_layout.prop = FloatProperty(  
        #    name="distance",  
        #    default=1.0,  
        #    subtype='DISTANCE',  
        #    unit='LENGTH',  
        #    description="distance"  
        #    ) 

        