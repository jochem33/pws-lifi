import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time

DATARATE = 0.24
currentTime = time.time()
previousTime = time.time()

sPort = '/dev/cu.usbmodem14101'

aSerialData = serial.Serial(sPort,115201)

receiving = True

bitcount = 0

# main loop
while receiving:
    currentTime = time.time()
    if(currentTime - previousTime > DATARATE):
        previousTime = currentTime
        print(" ", bitcount * (1/DATARATE), "b/s")
        bitcount = 0

    if (aSerialData.inWaiting()>0):

        sData = aSerialData.readline()
        bit = str(sData)[2]
        char = ""
        if(bit == "0"):
            char = "_"
        elif(bit == "1"):
            char = "▓"
        print(char, end='')
        bitcount+=1

        
