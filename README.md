This is the first released version of the Brute Force Gimkit Joiner.
Give any feedback on how my script could be improved please!

Download the script here:
[BruteForceGimkit.py](https://github.com/user-attachments/files/23736356/BruteForceGimkit.py)

**Change the paths inside of the script to match the location of your images! If you don't do this step, the script won't work!**

If you're on Windows, it is recommended to use .pyw instead of the standard .py to ensure the window won't interrupt the script. If you're on Linux, use PyInstaller or a Linux-specific packaging tool (like creating a .deb package) to prevent the window from appearing. Or if you're on MacOS, use PyInstaller with the --windowed flag to create a standard .app bundle.

_Read the description below for setting up the script and its modules._

## Installation of Python and Modules
Be sure to have Python installed onto your device, if not, download it from their official website:
https://www.python.org/downloads/

Be sure to have these following external modules installed for Python:

Pyautogui
Pillow
OpenCV-Python
Pathlib
If you don't have those modules, input these lines into your terminal:

Windows (Recommended Method):
- _python -m pip install pyautogui_
- _python -m pip install pillow_
- _python -m pip install opencv-python_
- _python -m pip install pathlib_

Linux/MacOS (Recommended Method):
- _python3 -m pip install pyautogui_
- _python3 -m pip install pillow_
- _python3 -m pip install opencv-python_
- _python3 -m pip install pathlib_

## Setting Up the Script

You will need to contain these 3 images for the script to function correctly; you can contain them here or screenshot them in the Gimkit Join screen—png images are recommended:
- GameCode
- Join
- YourName

If you chose to take screenshots, crop them similarly to the images above:
https://www.gimkit.com/join

To contain the "YourName" image, you have to join a Gimkit game and be at the name prompt; the easiest method is by creating your own game and then joining it as another player.

This is an optional step: you can rename the images to match the names in the script, if else, adjust the names inside of the script to match yours:

- _Join.png_

- _GameCode.png_

- _YourName.png_

This is another optional step: you can place all of the images inside of a folder to stay organized; you can match the folder name inside the script or change it to match yours:

- _Python_Images_

Now download the script itself:
[BruteForceGimkit.py](https://github.com/user-attachments/files/23736356/BruteForceGimkit.py)

If you're on Windows, it is recommended to use .pyw instead of the standard .py to ensure the window won't interrupt the script. If you're on Linux, use PyInstaller or a Linux-specific packaging tool (like creating a .deb package) to prevent the window from appearing. Or if you're on MacOS, use PyInstaller with the --windowed flag to create a standard .app bundle.

## !!IMPORTANT STEPS!!
**Change the paths inside of the script to match the location of your images! If you don't do this step, the script won't work!**

Finally, go to the Gimkit Join screen and run the script—everything should work according to plan:
https://www.gimkit.com/join
