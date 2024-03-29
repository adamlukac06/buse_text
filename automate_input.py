import pyautogui
import sys
import time
import pyperclip  # Added for clipboard operations

# Function to type text with case sensitivity
def type_text_sensitively(text):
    for char in text:
        if char in ['Á', 'É', 'Í', 'Ó', 'Ú', 'Ý', 'Č', 'Ď', 'Ľ', 'Ň', 'Ŕ', 'Š', 'Ť', 'Ž', 'á', 'é', 'í', 'ó', 'ú', 'ý', 'č', 'ď', 'ľ', 'ň', 'ŕ', 'š', 'ť', 'ž']:
            pyperclip.copy(char)  # Copy the special character to clipboard
            pyautogui.hotkey('ctrl', 'v')  # Paste the character
            time.sleep(0.05)  # Short delay to ensure the character is pasted before moving on
        elif char.isupper():
            pyautogui.keyDown('shift')  # Hold Shift for uppercase
            pyautogui.press(char.lower())  # Type the character in lowercase
            pyautogui.keyUp('shift')  # Release Shift
        elif char.isdigit():
            pyautogui.press(char)  # For digits, just press them
        else:
            pyautogui.press(char)  # Type the character as is

# The text to enter is passed as a command-line argument
text_to_enter = "aA1" + (sys.argv[1] if len(sys.argv) > 1 else "Default Text")

# Print the text to enter at this point
print(f"Text to enter (after prepending 'aA1'): {text_to_enter}")

# Coordinates of the entry field
entry_field_x, entry_field_y = 420, 1497  # Adjusted the Y coordinate

# Safety feature to prevent runaway scripts
pyautogui.FAILSAFE = True

# Optionally, wait a bit for the user to manually focus the window if needed
time.sleep(2)

# Move the mouse to the entry field and click
pyautogui.click(x=entry_field_x, y=entry_field_y)

# Print the text right before typing
print(f"Text right before typing: {text_to_enter}")

# Type the text with case sensitivity
type_text_sensitively(text_to_enter)

# Print after typing
print(f"Text after typing: {text_to_enter}")

# Press Enter
pyautogui.press('enter')
