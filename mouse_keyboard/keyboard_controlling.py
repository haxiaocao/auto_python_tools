# -*- coding: utf-8 -*-
# https://automatetheboringstuff.com/chapter18/

import pyautogui
import time


def type_string():
    pyautogui.click(1000, 1000)
    pyautogui.typewrite('I love you so much about this message.', 0.03)


''' you can search the key word to get the keyboard words. : PyAutoGUI keyboard  string'''


def type_key_names():
    pyautogui.click(1000, 1000)
    pyautogui.typewrite(['a', 'b', 'left', 'right', 'X', 'Y'], 0.05)


def press_and_release_keyboard():
    pyautogui.keyDown('shift')
    pyautogui.press('4')
    pyautogui.keyUp('shift')


def type_hot_key():
    pyautogui.click(100, 1000)
    pyautogui.typewrite('I love you , men.')
    time.sleep(2)
    pyautogui.hotkey('ctrl', '/')

# Handle Select Lists and Radio Buttons
# submit the form to the order and enter the keyboard.


# type_string()
# type_key_names()
# press_and_release_keyboard()
type_hot_key()
