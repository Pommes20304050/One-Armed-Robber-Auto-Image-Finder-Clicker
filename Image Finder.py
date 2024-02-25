import pyautogui
import win32api
import win32con
import keyboard
import sys
import time

def left_click(position):
    # Move mouse 20 pixels down
    win32api.SetCursorPos((position[0], position[1] + 20))
    
    # left click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def click_until_not_visible(target, confidence=0.4):
    while True:
        position = pyautogui.locateCenterOnScreen(target, confidence=confidence)
        if position:
            left_click(position)
        else:
            break

def quit_on_esc():
    print("Press 'Esc' to quit.")
    keyboard.wait('esc')
    sys.exit()

def main():
    targets = ['target1.png', 'target2.png']
    for target in targets:
        click_until_not_visible(target, confidence=0.4)
    
    quit_on_esc() 

if __name__ == "__main__":
    main()
