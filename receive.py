# from os import sync
# import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time

from constants import *

rx = serial.Serial(RECEIVINGDEVICE,BAUDRATE)



######## Wait till last 16 bits is the preamble, return if the bits are flipped or not #######
def findFrameStart():
    startTime = time.time()
    syncList = [2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2]
    while True:
        if (rx.inWaiting()>0):
            ##### Remove first item from synclist and append new bit
            del syncList[0]
            sData = rx.readline()
            bit = str(int(sData))
            syncList.append(bit)
            # print(syncList)

            ##### If framestart or reversed framestart is found, return true and if bits should be flipped
            if(syncList == FRAMESTART):
                return True, False
            if(syncList == ANTIFRAMESTART):
                return True, True

        ##### If timeout time has passed, return False for frame not found
        if(time.time() - startTime >= TIMEOUTTIME):
            print(syncList)
            return False, True



######## Read the payloadlenght + numberlenght bits and put them in payload string #######
def readPayload(flipped):
    payload = ""

    ##### Read payload while payload is not yet complete
    while len(payload) < PAYLOADLENGHT + PACKETNUMLENGHT:
        if (rx.inWaiting()>0):

            sData = rx.readline()
            symbol = '{0:04b}'.format(int(bytes(sData)))
            
            payload = payload + symbol
    return payload



######## Translate binary string and return payload in text #######
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))



###### Check if parity is correct ######
def checkFrame(frame):
    ##### split payload and framenumber
    payload = frame[:PAYLOADLENGHT + PACKETNUMLENGHT - PARITYLENGHT]
    binNumber = frame[PAYLOADLENGHT + PACKETNUMLENGHT - PARITYLENGHT:PAYLOADLENGHT + PACKETNUMLENGHT]

    ##### Calculate parity and parse packetnumber
    parityNumber = int(binNumber, 2)
    paritycount = len(payload[PACKETNUMLENGHT:].replace("0", ""))

    ##### correct frame (not yet written)
    correctedFrame = payload

    ##### if parity is correct, return true
    if(paritycount == parityNumber):
        return True, correctedFrame
    return False, correctedFrame



def readFrame():
    frameCorrect = False
    frameNumber = -1
    frame = ""
    ##### Synchronize and wait for framestart
    received, flipped = findFrameStart()
    ##### If framestart was found
    if(received):
        ##### Read payload
        binFrame = readPayload(flipped)
        print(binFrame)
        ##### Check frame, decode frame and parse framenumber
        frameCorrect, binFrame = checkFrame(binFrame)
        try:
            frame = decode_binary_string(binFrame[PACKETNUMLENGHT:])
        except:
            frame = "<unreadable frame>"
        try:
            frameNumber = int(binFrame[:PACKETNUMLENGHT], 2)
        except:
            frameNumber = -1

        return True, frameCorrect, frameNumber, frame
    else:
        return False, frameCorrect, frameNumber, frame


