import pyautogui
import time

def auto_clicker(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        pyautogui.click()
        time.sleep(interval)

# Parameters: interval between clicks (in seconds) and total duration (in seconds)
auto_clicker(0.1, 10)  # For example, clicks every 0.1 seconds for 10 seconds
