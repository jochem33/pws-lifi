import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time


DATARATE = 0.01

######## serial setup ######
ser = serial.Serial('/dev/cu.usbserial-1420', 115201, timeout=1)
############################



######## time setup #######
currentTime = time.time()
previousTime = time.time()
############################

list = [0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,1, 0,1,0,0,0,0,0,1, 0,1,1,1,0,0,0,0, 0,1,1,1,0,0,0,0, 0,1,1,0,0,1,0,1, 0,1,1,0,1,1,0,0, 0,1,1,0,1,1,0,0, 0,1,1,0,0,1,0,1, 0,1,1,0,1,0,1,1]


i = 0
while True:
    currentTime = time.time()

    if(currentTime - previousTime > DATARATE):
        previousTime = currentTime
        i+=1
        if(i==96):
            i = 0
        currentByte = bytes(str(list[i]), encoding='utf-8')
        ser.write(currentByte)
        print(currentByte)
        
