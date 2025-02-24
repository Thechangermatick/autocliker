import pyautogui
import time

def move_mouse(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        # Move the mouse to a new position
        pyautogui.move(100, 0, duration=0.25)  # Move right
        pyautogui.move(-100, 0, duration=0.25)  # Move left
        time.sleep(interval)

# Parameters: interval between movements (in seconds) and total duration (in seconds)
move_mouse(30, 3600)  # Move every 30 seconds for 1 hour
