"""
Description: This script provides classes for control of the UPS USB device.

Author: Adrian Rabadan

Date Created: May 16, 2024

Date Modified: Month DD, Year

Version: 1.0

Dependencies: hid
"""

from HID_Device import HID
import time
import json

class UPS:
    """
    Class to manage a UPS device using HID communication.

    Attributes:
        vendor_ID (int): Vendor ID of the UPS HID device.
        product_ID (int): Product ID of the UPS HID device.
        UPS (HID): Instance of the HID class to communicate with the UPS.
        print_output (bool): Flag to determine whether to print output messages.
    """
    def __init__(self, vendor_ID, product_ID, print_output):
        """
        Initializes the UPS class with the given vendor and product IDs.

        Args:
            vendor_ID (int): Vendor ID of the UPS HID device.
            product_ID (int): Product ID of the UPS HID device.
            print_output (bool): Flag to determine whether to print output messages.
        """
        self.vendor_ID = vendor_ID
        self.product_ID = product_ID
        self.UPS = HID(self.vendor_ID, self.product_ID, 0)
        self.print_output = print_output
   
    def powerON(self):
        """
        Powers on the UPS device by sending 'C' commands.
        """
        self.UPS.openHID()
        self.UPS.writeHID('0C')
        self.UPS.writeHID('0\r')
        self.UPS.closeHID() 
    
    def instantShutDown(self):
        """
        Instantly shuts down the UPS device by sending 0S00R0000 command.
        """
        self.UPS.openHID()
        self.UPS.writeHID('0S00R0000')
        self.UPS.writeHID('0\r0000000')
        self.UPS.closeHID()

    def afters18secShutDown(self):
        """
        Shuts down the UPS device after 18 seconds by sending 0S.3R0000 command.
        """
        self.UPS.openHID()
        self.UPS.writeHID('0S.3R0000')
        self.UPS.writeHID('0\r0000000')
        self.UPS.closeHID()
        
    def after1minRestart(self):
        """
        Restarts the UPS device after 1 minute by sending '0S01R0001' command.
        """
        self.UPS.openHID()
        self.UPS.writeHID('0S01R0001')
        self.UPS.writeHID('0\r0000000')
        self.UPS.closeHID()
    
    def after18secRestart(self):
        """
        Restarts the UPS device after 18 seconds by sending '0S.3R0001'' command.
        """
        self.UPS.openHID()
        self.UPS.writeHID('0S.3R0001')
        self.UPS.writeHID('0\r0000000')
        self.UPS.closeHID()
        
    def customShutdown(self, wtime):
        """
        Shuts down the UPS device after a custom time by sending the wtime command. 

        For example:
        - If `wtime = '0S.1R0000'`, the UPS will shut down after waiting 6 seconds.
        - If `wtime = '0S.2R0000'`, the UPS will shut down after waiting 12 seconds.
        - If `wtime = '0S02R0000'`, the UPS will shut down after 2 minutes.

        Args:
            wtime (str): The wait time command string to send to the UPS device.
        """
        self.UPS.openHID()
        self.UPS.writeHID(wtime)
        self.UPS.writeHID('0\r0000000')
        self.UPS.closeHID()
        
    def getStatus(self):
        """
        Retrieves the current status of the UPS device.

        Returns:
            str: JSON-formatted string containing the status information of the UPS device: Vin, Vout, Freq, Mode, Vbat.
        """
        respuesta = []
        num_bytes = 20
        self.texto_decodificado = ""
        self.UPS.openHID()
        self.UPS.writeHID('0QS')
        self.UPS.writeHID('0\r0')
        time.sleep(0.1)
        
        # Save response
        for i in range(num_bytes):
            respuesta.append(self.UPS.readHID(num_bytes))
        
        self.UPS.closeHID()
           
        # Decode the byte array to a text string
        for bytes_lista in respuesta:
            self.texto_decodificado += ''.join(chr(byte) for byte in bytes_lista)

        # Display the decoded text
        if self.print_output: 
            print("Texto decodificado:")
            print(self.texto_decodificado)

        # Split the data into separate partss
        partes = self.texto_decodificado.split()
        
        if partes[3] == '000':
            partes[3] = 'Line Mode'
        if partes[3] == '001':
            partes[3] = 'Battery Mode'

        # Create a structured data dictionary
        estructura_datos = {
            "V": partes[0] + ' V',
            "Vin": partes[1]+ ' V',
            "Vout": partes[2]+ ' V',
            "Modo": partes[3],
            "Freq": partes[4]+ ' Hz',
            "VBatt": partes[5] + ' V',
            "--": partes[6],
            "Id": partes[7]
        }

        # Display the structured data
        if self.print_output: 
            print("Estructura con los datos divididos:")
            print(estructura_datos)

        # Convert the structure to JSON format
        self.json_output = json.dumps(estructura_datos, indent=4)

        return self.json_output

    def batteryTest(self):
        """
        Initiates a battery test on the UPS device by sending b'T' command.
        """
        self.UPS.openHID()
        self.UPS.writeHID('0T')
        self.UPS.writeHID('0\r')
        self.UPS.closeHID()
    
    def toogleBeeper(self):
        """
        Toggles the beeper on the UPS device by sending b'Q' command.
        """
        self.UPS.openHID()
        self.UPS.writeHID('0Q')
        self.UPS.writeHID('0\r')
        self.UPS.closeHID()    
    
#Example usage
UPS = UPS(0x0665,0x5161,0)
#time.sleep(2)
#UPS.powerON()
#UPS.afters18secShutDown()
#UPS.after1minRestart()
#UPS.customShutdown('0S.2R0000')
#UPS.customShutdown('0S02R0000')
print(UPS.getStatus())
#UPS.batteryTest()
#UPS.toogleBeeper()
#UPS.instantShutDown()
