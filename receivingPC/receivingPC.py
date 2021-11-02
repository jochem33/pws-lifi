import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time

DATARATE = 0.25
currentTime = time.time()
previousTime = time.time()

sPort = '/dev/cu.usbmodem14201'

aSerialData = serial.Serial(sPort,115201)

receiving = True

bitcount = 0

# main loop
while receiving:
    currentTime = time.time()
    if(currentTime - previousTime > DATARATE):
        previousTime = currentTime
        print( 20 * "\n", bitcount *4, "b/s")
        bitcount = 0

    if (aSerialData.inWaiting()>0):

        sData = aSerialData.readline()
        bit = str(sData)[2]
        bitcount+=1

        
