import pyautogui
import sys
import time

# The text to enter is passed as a command-line argument
text_to_enter = sys.argv[1] if len(sys.argv) > 1 else "Default Text"

# Coordinates of the entry field
entry_field_x, entry_field_y = 420, 1497  # Adjusted the Y coordinate

# Safety feature to prevent runaway scripts
pyautogui.FAILSAFE = True

# Optionally, wait a bit for the user to manually focus the window if needed
time.sleep(2)

# Move the mouse to the entry field and click
pyautogui.click(x=entry_field_x, y=entry_field_y)

# Type the text
pyautogui.typewrite(text_to_enter, interval=0.05)

# Press Enter
pyautogui.press('enter')
