import warnings
import serial
import serial.tools.list_ports
from serial import Serial


sPort = '/dev/cu.usbmodem14101'

aSerialData = serial.Serial(sPort,115201)

receiving = True


# main loop
while receiving:
    # if serial data is found
    if (aSerialData.inWaiting()>0):

        # get bits
        sData = aSerialData.readline()
        bit = str(sData)[2]
        print(bit)

        
