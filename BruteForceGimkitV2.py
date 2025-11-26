import pyautogui
import random
import time
import pathlib
pyautogui.PAUSE = 0
Home = pathlib.Path.home()

# Adjust paths according to the location of your images
Join = str(Home / "Desktop" / "Python_Images" / "Join.png")
GameCode = str(Home / "Desktop" / "Python_Images" / "GameCode.png")
Misses = 0

while True:
    while True:
        try:
            Misses = 0
            Location = pyautogui.locateCenterOnScreen(GameCode, confidence=0.8) # Looks for Game Code, adjust confidence if needed
            x, y = Location
            pyautogui.moveTo(x, y, duration=0)
            pyautogui.click()
            Code = ''.join(random.choice('0123456789') for _ in range(6))
            pyautogui.write(Code)
            break
        except pyautogui.ImageNotFoundException: # Checks if name prompt isn't on screen
            Misses += 1
            if Misses > 14: # Adjust miss limit if needed
                exit()
            pass
  
    while True:
        try:
            Location = pyautogui.locateCenterOnScreen(Join, confidence=0.8) # Looks for Join Button, adjust confidence if needed
            x, y = Location
            pyautogui.moveTo(x, y, duration=0)
            pyautogui.click()
            break
        except pyautogui.ImageNotFoundException:
            pass
