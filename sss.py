import pyautogui
import time
import pydirectinput
import win32api
import win32con
while True:
    time.sleep(4)
    pydirectinput.keyDown("w")
    time.sleep(1)
    pydirectinput.keyDown("w")
    time.sleep(4)
    #wwpydirectinput.click(200,200)
    #pydirectinput.moveRel(0,0)
    #wpydirectinput.click(0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -200, 0, 200,200)
    time.sleep(0.1)
    pydirectinput.click()