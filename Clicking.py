import pyautogui
import time

# click locations: 1480, 250 => 1650, 390
pyautogui.moveTo(1650, 390)

try:
    for i in range(0, 1000):
        position = pyautogui.position()
        time.sleep(0.2)
        if pyautogui.position() != position:
            raise RuntimeError("Failsafe activated")
        pyautogui.click()
        time.sleep(0.05)
        pyautogui.moveTo(1480, 250)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.05)
        pyautogui.moveTo(1650, 390)
except RuntimeError as message:
    print(message)