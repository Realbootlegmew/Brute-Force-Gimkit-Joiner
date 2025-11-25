import pyautogui
import random
import time
import pathlib
pyautogui.PAUSE = 0
Home = pathlib.Path.home()

# Adjust paths according to the location of your images
Join = str(Home / "Desktop" / "Python_Images" / "Join.png")
GameCode = str(Home / "Desktop" / "Python_Images" / "GameCode.png")
YourName = str(Home / "Desktop" / "Python_Images" / "YourName.png")

while True:
    try:
        Location = pyautogui.locateOnScreen(YourName, confidence=0.8) # Looks for name prompt, adjust confidence if needed
        if Location:
            print("Attempt was successful.")
            break
    except pyautogui.ImageNotFoundException: # If the name prompt is not found, the code runs brute force

        while True:
            try:
                Location = pyautogui.locateCenterOnScreen(GameCode, confidence=0.8) # Looks for Game Code, adjust confidence if needed
                x, y = Location
                pyautogui.moveTo(x, y, duration=0)
                pyautogui.click()
                Code = ''.join(random.choice('0123456789') for _ in range(6))
                pyautogui.write(Code)
                break
            except pyautogui.ImageNotFoundException:
                time.sleep(0)
  
        while True:
            try:
                Location = pyautogui.locateCenterOnScreen(Join, confidence=0.8) # Looks for Join Button, adjust confidence if needed
                x, y = Location
                pyautogui.moveTo(x, y, duration=0)
                pyautogui.click()
                break
            except pyautogui.ImageNotFoundException:
                time.sleep(0)



