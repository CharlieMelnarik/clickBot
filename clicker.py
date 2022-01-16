from pynput.mouse import Button, Controller as MouseController
import time
from datetime import datetime


mouse = MouseController()


def click():
    mouse.press(Button.left)
    mouse.release(Button.left)

while True:
    times = datetime.now()
    hour = times.hour
    minute = times.minute
    second = times.second
    millisecond = times.microsecond
    Range = range(0, 200000)
    if hour == 13 and minute == 36 and second == 0 and millisecond in Range:
        click()
        break
