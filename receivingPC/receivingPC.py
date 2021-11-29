from os import sync
import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time

FRAMESIZE = 64
# DATARATE = 0.24
currentTime = time.time()
previousTime = time.time()

FRAMASTART = ["0","0","0","0","0","0","0","0", "0","0","0","0","0","0","0","1"]
ANTIFRAMASTART = ["1","1","1","1","1","1","1","1", "1","1","1","1","1","1","1","0"]


sPort = '/dev/cu.usbmodem14101'

aSerialData = serial.Serial(sPort,115201)

receiving = False


        
def findFrameStart():
    unSynced = True
    syncList = [2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2]
    while unSynced:
        if (aSerialData.inWaiting()>0):
            del syncList[0]
            sData = aSerialData.readline()
            bit = str(sData)[2]
            syncList.append(bit)
            if(syncList == FRAMASTART):
                print("Found, normal")
                return False
            elif(syncList == ANTIFRAMASTART):
                print("Found, flipped")
                return True

        
def readFrame(flipped):
    payload = ""
    while len(payload) < FRAMESIZE:
        # currentTime = time.time()
        # if(currentTime - previousTime > DATARATE):
        #     previousTime = currentTime
        #     print(" ", bitcount * (1/DATARATE), "b/s")
        #     bitcount = 0

        if (aSerialData.inWaiting()>0):

            sData = aSerialData.readline()
            bit = str(sData)[2]
            if(flipped):
                bit = int(bit) * -1 + 1
            payload = payload + str(bit)
    return payload


def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

while True:
    flipped = findFrameStart()

    frame = readFrame(flipped)
    print(frame)

    print(decode_binary_string(frame))




