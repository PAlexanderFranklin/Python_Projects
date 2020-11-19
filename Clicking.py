import pyautogui
import time

clickList = [] # (x position of click, y position of click, time delay in seconds)
clickList.append([1480, 250, 0.05])
clickList.append([1650, 280, 0.05])

def repeatClicks(clickList, repeats):
    try:
        for n in range(0, repeats):
            for i in clickList:
                pyautogui.moveTo(i[0], i[1])
                position = pyautogui.position()
                time.sleep(i[2])
                if pyautogui.position() != position:
                    raise RuntimeError("Mouse moved by user, activating failsafe.")
                pyautogui.click()
    except RuntimeError as message:
        print(message)

repeatClicks(clickList, 50)