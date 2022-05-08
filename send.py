# from os import sync
# import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time

from constants import *

tx = serial.Serial(SENDINGDEVICE,BAUDRATE)



######## time setup #######
currentTime = time.time()
previousTime = time.time()
############################



######## send nothing #######
def frameGap(i):
    d=0


######## send 0's and one 1 #######
def preamble(i):
    if(i *4 < PREAMBLELENGHT - 4):
        intSymbol = int(str(("0101")), 2)
        currentByte = intSymbol.to_bytes(1, 'big')
        tx.write(currentByte)
    else:
        intSymbol = int(str("0001"), 2)
        currentByte = intSymbol.to_bytes(1, 'big')
        tx.write(currentByte)



######## send packetnumber ####### 
###### this function may be removed because its the same as the 'payload' function
def packetNumber(i, bit):
    intSymbol = int(str(bit[i*4:i*4+4]), 2)
    currentByte = intSymbol.to_bytes(1, 'big')
    tx.write(currentByte)




######## send payload #######
def payload(i, data):
    intSymbol = int(str(data[i*4:i*4+4]), 2)
    currentByte = intSymbol.to_bytes(1, 'big')
    tx.write(currentByte)


def ones(i, data):
    intSymbol = int(str(data[i*4:i*4+4]), 2)

    currentByte = intSymbol.to_bytes(1, 'big')

    tx.write(currentByte)
    # print(str(data[i*4:i*4+4]), intSymbol, currentByte, int.from_bytes(currentByte, byteorder='big'))





######## call <callback> funtion <count> times at the interval of DATARATE #######
def repeatInterval(callback, count, arg=None):
    previousTime = time.time()
    i = 0
    while i < count:
        currentTime = time.time()

        ###### if enough time for next bit has passed
        if(currentTime - previousTime > DATARATE):
            previousTime = currentTime

            ###### call callback funtion and pass argument if argument is present
            if(arg is not None):
                callback(i, arg)
            else:
                callback(i)
            i+=1





def sendFrame(payloadstr, frameIndex):
    payloaddata = "".join(f"{ord(i):08b}" for i in payloadstr)
    payloaddata = payloaddata[:PAYLOADLENGHT]
    
    ##### Add parity
    paritycount = len(payloaddata.replace("0", ""))
    binparitycount = '{0:016b}'.format(paritycount)
    payloaddata = payloaddata + ((PARITYLENGHT - len(str(binparitycount))) * "0") + binparitycount

    ##### Make binary frameIndex
    frameIndex16bin = '{0:016b}'.format(frameIndex)

    ###### every phase of the entire frame
    repeatInterval(frameGap, GAPLENGHT)
    repeatInterval(preamble, PREAMBLELENGHT / 4)
    repeatInterval(packetNumber, PACKETNUMLENGHT / 4, frameIndex16bin)
    repeatInterval(payload, PAYLOADLENGHT / 4, payloaddata)

    # repeatInterval(ones, PAYLOADLENGHT / 4, payloaddata)