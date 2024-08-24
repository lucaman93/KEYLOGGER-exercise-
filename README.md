Importing keyboard from pynput:
This module is used to monitor and control keyboard inputs. It allows the script to detect when keys are pressed or released, making it essential for building keyloggers.

Path to Store Keystrokes:
The keyfile_path variable stores the path to the file (keylog.txt) where the recorded keystrokes will be saved. This file will be created or appended with new data whenever keys are pressed.

on_press() Function:
This function handles keystrokes when a key is pressed. It uses a try-except block to differentiate between regular character keys and special keys (like Ctrl, Alt, etc.).
This approach ensures that all types of key presses are logged, and it avoids errors when trying to log special keys.

on_release() Function:
This function stops the listener when the Escape key is pressed.
This provides a way to terminate the keylogger gracefully. Without this, the keylogger would continue running indefinitely.

Starting the Listener:
The keyboard.Listener starts the keylogging process and listens for both key presses and releases.
Why this approach? This is the core functionality of the script, allowing it to capture and log keystrokes continuously.
