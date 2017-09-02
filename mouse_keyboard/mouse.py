# -*- coding: utf-8 -*-
# https://automatetheboringstuff.com/chapter18/

import pyautogui
import time

# print 'press the ctrl-c to quit this program'


def mouse_position_showing():
    try:
        while True:
            # todo：get and print the mouse coordinates
            x, y = pyautogui.position()
            position_str = 'x:{},y:{}'.format(
                str(x).rjust(4), str(y).rjust(4))
            print position_str
            time.sleep(1)
    except KeyboardInterrupt:
        print '\nDone'


def mouse_drag():
    time.sleep(5)
    pyautogui.click()
    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2)  # move right
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.2)  # move down
        pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
        distance = distance - 5
        pyautogui.dragRel(0, -distance, duration=0.2)  # move up


def mouse_scroll():
    time.sleep(5)
    print 'now begin to scroll'
    pyautogui.scroll(20000)


def screenshot():
    im = pyautogui.screenshot()
    print im.getpixel((100, 1000))
    x, y = 100, 1000
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    pixelColor = pyautogui.screenshot().getpixel((x, y))
    positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
    positionStr += ', ' + str(pixelColor[1]).rjust(3)
    positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
    print positionStr

# mouse_position_showing()
# mouse_drag()
# mouse_scroll()
# screenshot()
