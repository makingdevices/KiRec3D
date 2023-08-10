import time
import win32api
import win32con

import ctypes
from ctypes import wintypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

def keyb(ch=None,shift=False,control=False,alt=False, delaik=0.02):
    for b in ch:
        c=b
        if (b>='A' and b<='Z') or shift:
            win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
        if b>='a' and b<='z':
            c=b.upper()
        if alt:
            win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)
            time.sleep(0.250)
        if control:
            win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
        if isinstance(b,(int)):
            cord=b
        else:
            cord=ord(c)

        win32api.keybd_event(cord, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
        if delaik>0.0:
            time.sleep(delaik)
        win32api.keybd_event(cord, 0, win32con.KEYEVENTF_EXTENDEDKEY |
win32con.KEYEVENTF_KEYUP, 0)
        if delaik>0.0:
            time.sleep(delaik)

        if control:
            win32api.keybd_event(win32con.VK_CONTROL, 0,
win32con.KEYEVENTF_KEYUP, 0)
        if alt:
            win32api.keybd_event(win32con.VK_MENU, 0,
win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.05)
        if (b>='A' and b<='Z') or shift:
            win32api.keybd_event(win32con.VK_SHIFT, 0,
win32con.KEYEVENTF_KEYUP, 0)


def move3D(middle_x, middle_y, middle_movement):
    x = middle_x
    y = middle_y
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0) #Press click button down
    x = x + middle_movement
    win32api.SetCursorPos((x, y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0) #Press click button up

def saveimage(savex,savey,savepng,i):
    x = savex
    y = savey
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0) #Press click button down
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0) #Press click button up
    y = savepng
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0) #Press click button down
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0) #Press click button up
    time.sleep(0.2)
    keyb("pic"+str(i))
    keyb("\r")

def read_config(filename):
    f = open(filename)
    config_dict = {}
    for lines in f:
        try:
            items = lines.split(': ', 1)
            config_dict[items[0]] = eval(items[1])
        except:
            pass
    return config_dict

data = read_config('config.txt')
time.sleep(data['var_init'])
var = 0
if __name__ == '__main__':
    for var in range(data['var_number']):
        saveimage(data['save_x'],data['save_y'],data['save_png'],var)
        time.sleep(1)
        var = var +1
        move3D(data['main_screen_x'],data['main_screen_y'],data['main_screen_increment'])
        time.sleep(data['var_waitrender'])
        #time.sleep(1)
        #move3D()

