"""
Description: This script provides classes for control of the HID USB device.

Author: Adrian Rabadan

Date Created: May 16, 2024

Date Modified: Month DD, Year

Version: 1.0

Dependencies: hid
"""

import hid

class HID:
    """
    Class to handle the HID USB device.
    
    This class includes methods to open, close, read from, and write to the HID device.

    Attributes:
        vendor_ID (int): Vendor ID of the HID device.
        product_ID (int): Product ID of the HID device.
        print_output (bool): Flag to print output messages.
        handle: HID device handle.
        num_bytes (int): Number of bytes to read from the HID device.
    """
    def __init__(self, vendor_ID, product_ID, print_output = True):
        """
        Initializes the HID class with the given vendor and product IDs.

        Args:
            vendor_ID (int): Vendor ID of the HID device.
            product_ID (int): Product ID of the HID device.
            print_output (bool, optional): Flag to print output messages. Default is True.
        """
        self.vendor_ID = vendor_ID
        self.product_ID = product_ID
        self.print_output = print_output
        self.handle = None
        self.num_bytes = 20

    def openHID(self):
        """
        Opens the HID device if it is not already opened.

        Returns:
            bool: True if the device was successfully opened, False otherwise.
        """
        if not self.handle:
            devices = hid.enumerate()
            hid_device = next((device for device in devices if device['vendor_id'] == self.vendor_ID and device['product_id'] == self.product_ID), None)

            if hid_device is None:
                if self.print_output: print("HID device not found")
                return False
            
            try:
                # Open HID device
                self.handle = hid.device()
                self.handle.open(self.vendor_ID, self.product_ID)
                if self.print_output: print("HID Device has been opened!")
                return True
            except Exception as e:
                if self.print_output: print("Error trying to open the HID device:", e)
                return False
        else:
            if self.print_output: print("HID Device is already open!")
            return True

    def closeHID(self):
        """
        Closes the HID device if it is opened.
        """
        if self.handle:
            self.handle.close()
            if self.print_output: print("HID Device has been closed!")
            self.handle = None
        else:
            if self.print_output: print("No HID Device to close!")

    def readHID(self, numBytes):
        """
        Reads data from the HID device.

        Args:
            numBytes (int): Number of bytes to read from the device.

        Returns:
            list: Data read from the device.
        """
        if self.handle:
            data = self.handle.read(numBytes)
            return data
        else:
            if self.print_output: print("HID Device not open!")
            return []

    def writeHID(self, command): 
        """
        Writes data to the HID device.

        Args:
            command (str or bytes): Command to be written to the device.
        """
        if self.handle:  
            # Convert the command to bytes if it is not already
            comando = command.encode() if isinstance(command, str) else command 
            if self.print_output: print("Command received: ", comando)
            self.handle.write(comando)
        else:
            if self.print_output: print("HID Device not open!")

# Example usage
# UPS = HID(0x0665, 0x5161)
# UPS.openHID()
# UPS.writeHID('0C')
# UPS.writeHID('0\r')
# UPS.closeHID()
#
# UPS.openHID()
# UPS.writeHID('0S00R0000')
# UPS.writeHID('0\r0000000')
# UPS.closeHID()

