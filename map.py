import pyautogui
import time

print("Move the mouse over the target area and press Ctrl+C to display the coordinates.")

try:
    while True:
        # Print the current mouse coordinates
        x, y = pyautogui.position()
        print(f"Position: {x}, {y}", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nDone.")
