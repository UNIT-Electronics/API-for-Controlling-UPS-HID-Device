# API for Controlling UPS HID Device

## Description

This repository contains a Python API for controlling an Uninterruptible Power Supply (UPS) using the Human Interface Device (HID) protocol. It provides a set of classes and methods to manage the UPS device through USB communication. The API includes functionalities to power on/off the UPS, perform shutdowns and restarts with custom timings, retrieve the status of the UPS, and initiate a battery test.

## Author

- **Name:** Adrian Rabadan
- **Date Created:** May 16, 2024

## Version

- **Version:** 1.0

## Dependencies

- **Python libraries:** `hid`
  ```sh
  pip install hidapi

## Files

1. QueryUPS.py
This script contains the UPS class which provides methods to control the UPS device.

2. HID_Device.py
This script contains the HID class which handles the HID USB device communication.

## Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/API-for-controlling-UPS-HID-device.git

2. **Navigate to the project directory:**
    ```sh
    cd API-for-controlling-UPS-HID-device

3. **Install dependencies:**
    ```sh
    pip install hidapi

## Usage

### Example

Here's an example of how to use the API to get the status of the UPS and perform a shutdown.

```python
from QueryUPS import UPS

# Initialize the UPS object with Vendor ID and Product ID
ups = UPS(0x0665, 0x5161, print_output=True)

# Get the status of the UPS
print(ups.getStatus())

# Shutdown the UPS instantly
ups.instantShutDown()

```
## Available Commands

| Command                | Description                                                      |
|------------------------|------------------------------------------------------------------|
| `powerON`              | Powers on the UPS device by sending 'C' commands.                |
| `instantShutDown`      | Instantly shuts down the UPS device by sending `0S00R0000` command.|
| `afters18secShutDown`  | Shuts down the UPS device after 18 seconds by sending `0S.3R0000` command. |
| `after1minRestart`     | Restarts the UPS device after 1 minute by sending `0S01R0001` command. |
| `after18secRestart`    | Restarts the UPS device after 18 seconds by sending `0S.3R0001` command. |
| `customShutdown`       | Shuts down the UPS device after a custom time specified by `wtime` command. |
| `getStatus`            | Retrieves the current status of the UPS device. Returns a JSON-formatted string. |
| `batteryTest`          | Initiates a battery test on the UPS device by sending `0T` command. |
| `toggleBeeper`         | Toggles the beeper on the UPS device by sending `0Q` command.     |

## HID Commands Table

| Command         | Description                            |
|-----------------|----------------------------------------|
| `0C`            | Power on command.                      |
| `0S00R0000`     | Instant shutdown command.              |
| `0S.3R0000`     | Shutdown after 18 seconds command.     |
| `0S01R0001`     | Restart after 1 minute command.        |
| `0S.3R0001`     | Restart after 18 seconds command.      |
| `0T`            | Battery test command.                  |
| `0Q`            | Toggle beeper command.                 |
| `0QS`           | Get status command.                    |
| `custom command`| Custom shutdown command with `wtime`.  |


# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
Special thanks to the developers of the hidapi library.