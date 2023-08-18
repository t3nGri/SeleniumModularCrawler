import win32api
import pywinauto
import time

time.sleep(5)

x, y = win32api.GetCursorPos()
print(x,y)

x, y = win32api.GetCursorPos()
print(x,y)