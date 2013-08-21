""" Handles the right import of the right files dependent on the OS. """

from sys import platform
import sys 
import os
import struct

# Import files from this folder.
sys.path.append(os.path.dirname(__file__))

# Determine architecture.
arch = struct.calcsize('P')*8
if arch == 64:
    arch = "x64"
elif arch == 32:
    arch = "x86"
else:
    raise Exception("Your architecture is not supported.")

def import_relative(path):
    sys.path.append(os.path.join(os.path.dirname(__file__), path))

# Support custom libaries (let users compile own libaries). 
import_relative(os.path.join("LeapPython", "custom"))

# Import platform relative leap libs.
# For other platforms only custom libaries are supported.
if platform == "darwin":  # Mac OS X
    import_relative(os.path.join("LeapPython", "mac", arch))
elif platform.startswith("win"):
    import_relative(os.path.join("LeapPython", "windows", arch))
else:
    print("Note (Leap Blender): For your OS only custom libaries are supported." \
" You will have to compile them manual and place them into the custom folder." \
" See the README file.")