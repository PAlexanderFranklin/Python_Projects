import pyautogui
import time

# click locations: 1480, 250 => 1650, 390

try:
    for i in range(0, 1000):
        position = pyautogui.position()
        time.sleep(0.05)
        if pyautogui.position() != position:
            raise RuntimeError("Failsafe activated")
except RuntimeError as message:
    print(message)