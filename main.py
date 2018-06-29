from detection import detect
from screenshot import secreenshot
import killswitch

import time
import win32api, win32con

IMAGE_FOLDER = 'images/'
TARGET_FILENAME = IMAGE_FOLDER + 'ball.PNG'
SCREENSHOT_FILENAME = IMAGE_FOLDER + 'screenshot.PNG'

desiredScore = 1000
currentActions = 0

emulatorLocation = {'left': 0, 'top': 0, 'width': 125, 'height': 225}

# Number of pixels under ball center to click
PIXBUFFER = 10

# Prevens spam clicking
SLEEPNUM = 0.4 


# Pass in x, y coordinates for mouse to click
# only works in windows
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


while currentActions < desiredScore:
    # take screenshot and save it in desired location
    secreenshot(emulatorLocation['left'], emulatorLocation['top'], 
                emulatorLocation['width'], emulatorLocation['height'],
                fileName=SCREENSHOT_FILENAME)

    # determine where center of ball is in screenshot
    centerX, centerY = detect(TARGET_FILENAME, SCREENSHOT_FILENAME)

    # if ball is near bottom half of screen, its okay to click
    # (prevents ball from traveling too far vertically)
    if centerY > (emulatorLocation['height'] - emulatorLocation['top']) / 2:
        click(centerX, centerY + PIXBUFFER)

        # sleep to prevent spamming
        time.sleep(SLEEPNUM)
        currentActions += 1
        print currentActions