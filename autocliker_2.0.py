import pyautogui
import time

pyautogui.FAILSAFE = False

while(1 != 0):
    width, height = pyautogui.size()
    pyautogui.click(width/2, height/2)
    time.sleep(10) # 10 seconds