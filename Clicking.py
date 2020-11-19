import pyautogui
import time

clickList = [] # (x position of click, y position of click, time delay in seconds)
clickList.append({'x': 1480, 'y': 250, 't': 0.2})
clickList.append({'x': 1650, 'y': 390, 't': 0.2})

try:
    for i in clickList:
        pyautogui.moveTo(i['x'], i['y'])
        position = pyautogui.position()
        time.sleep(i['t'])
        if pyautogui.position() != position:
            raise RuntimeError("Failsafe activated")
        pyautogui.click()
except RuntimeError as message:
    print(message)