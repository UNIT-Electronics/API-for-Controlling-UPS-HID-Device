from HID_Device import HID
import time 


NewRespuesta = []
num_bytes = 20

def readData():
    KEYboard.openHID()
    respuesta = KEYboard.readHID(num_bytes)
    KEYboard.closeHID()
    return respuesta
    


KEYboard = HID(0x0079,0x181c , 0)     
#KEYboard = HID(0x28DA,0x1102, 0)    

OldRespuesta = readData()

while True:
    NewRespuesta = readData()  
    if OldRespuesta != NewRespuesta:
        OldRespuesta = NewRespuesta
        print(NewRespuesta)

    