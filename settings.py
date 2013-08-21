""" Stores the settings of the Project. """

# How often to look for leap frames in a second.
framerate = 1/240

# Conversion factor by what to convert leap direction units to blender units.
lb_factor = 0.1

# Conversion factor by what to convert leap direction units to degree.
ld_factor = 0.01

# To compensate the Leap Y Axis which begins by 0.
leap_y_offset = -10

KeyTap_MinDownVelocity = 0.1  # Default: 50
KeyTap_HistorySeconds = 0.2  # Default: 0.1
KeyTap_MinDistance = 0.5     # Default: 5.0

# Lock KeyTap gesture in seconds to prevent double KeyTap presses.
key_tap_seconds_lock = 2
max_x = 80
max_y = 80
max_z = 50

"""
Leap Axis --> Blender Axis
X == Y --> horizontal
Z == X 
Y == Z (Leap Axis just positive values) --> vertical
"""