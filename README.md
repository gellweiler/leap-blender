Leap Blender only directly supports Windows. It might not work with every blender version, we only tested it with Blender 2.68.
If you have other requirements you will have to compile the LeapPython library for python yourself and put it into "LeapPython/custom".
But notice that Mac support is currently impossible. See the links at the bottom for further information.

Installation
--------------

1. If you dont have a zip file, compress the folder as zip
2. Open Blender and go under File --> User Preferences --> Addons and use "Install from file" to select the zip file.
3. Check the addon "3D View: Leap Blender".

Start the addon
--------------

(If you haven't started the Leap Controller or Control panel start it. In linux you have to run leapd in a terminal.)
Press the Space key and type Leap Blender and confirm with enter.

How to use
--------------

- Activate/deactivate the addon with a keytab.
- Move your hand with fingers spread ...
    - ... up and down to rotate horizontally.
    - ... left and right to rotate vertically.
    - ... forward and backward to zoom in and out-
- Make a fist to move selected objects.
- Move two Hands with fingers spread ...
    - ... up and down to rotate selected objects horizontally.
    - ... left and right to rotate selected objects vertically.
- Make two fists to move the workspace.

Links
--------------
- Compiling:
    - http://developer.leapmotion.com/articles/generating-a-python-3-3-0-wrapper-with-swig-2-0-9
    - http://www.warp1337.com/content/leap-motion-sdk-python3-python-33-ubuntu
    - http://developer.leapmotion.com/questions/can-leap-python-works-with-python-3-3-0-for-blender

- Mac:
    - http://blenderartists.org/forum/showthread.php?284076-Blender-crashes-at-module-import
    - http://blenderartists.org/forum/showthread.php?304359-Leap-frames-into-Mac-Blender-via-Client-Server
    - http://blenderartists.org/forum/showthread.php?273567-Leap-Motion-Blender-Integration-Help
    - http://developer.leapmotion.com/questions/blender-for-mac
    - http://developer.leapmotion.com/forums/forums/10/topics/leap-use-for-mac-blender-users

Suggestions for improvement
--------------
- Rewrite code to use the LeapMotion socket server instead of the python libraries to work around compatibility issues.
