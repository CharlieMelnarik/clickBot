from pynput.mouse import Button, Controller as MouseController
import time
from datetime import datetime
import pyautogui


mouse = MouseController()


def click():
    mouse.press(Button.left)
    mouse.release(Button.left)

Screenshot = pyautogui.screenshot()

while True:
    times = datetime.now()
    hour = times.hour
    minute = times.minute
    second = times.second
    millisecond = times.microsecond
    Range = range(0, 200000)
    if hour == 20 and minute == 8 and second == 0 and millisecond in Range:
        click()
        Screenshot.save(r'/Users/charliemelnarik/desktop/screenshot.png')
        break
