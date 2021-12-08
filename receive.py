from os import sync
import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time

from constants import *

rx = serial.Serial(RECEIVINGDEVICE,115201)



######## Wait till last 16 bits is the preamble, return if the bits are flipped or not #######
def findFrameStart():
    startTime = time.time()
    unSynced = True
    syncList = [2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2]
    while unSynced:
        if (rx.inWaiting()>0):
            del syncList[0]
            sData = rx.readline()
            bit = str(sData)[2]
            syncList.append(bit)
            if(syncList == FRAMESTART):
                return True, False
            if(syncList == ANTIFRAMESTART):
                return True, True
        if(time.time() - startTime >= TIMEOUTTIME):
            return False, True



######## Read the payloadlenght + numberlenght bits and put them in payload string #######
def readPayload(flipped):
    payload = ""
    while len(payload) < PAYLOADLENGHT + PACKETNUMLENGHT:
        if (rx.inWaiting()>0):

            sData = rx.readline()
            bit = str(sData)[2]
            if(flipped):
                bit = int(bit) * -1 + 1
            payload = payload + str(bit)
    return payload



######## Translate binary string and return payload in text #######
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))



###### Check if parity is correct ######
def checkFrame(frame):
    frameCorrect = False
    payload = frame[:PAYLOADLENGHT + PACKETNUMLENGHT - PARITYLENGHT]
    binNumber = frame[PAYLOADLENGHT + PACKETNUMLENGHT - PARITYLENGHT:PAYLOADLENGHT + PACKETNUMLENGHT]

    parityNumber = int(binNumber, 2)
    paritycount = len(payload[PACKETNUMLENGHT:].replace("0", ""))
    correctedFrame = payload

    # print("frame", frame, "binNum", binNumber, "parityNumber", parityNumber, "count", paritycount, "len", PAYLOADLENGHT - PARITYLENGHT + PACKETNUMLENGHT)
    if(paritycount == parityNumber):
        frameCorrect = True
    return frameCorrect, correctedFrame



def readFrame():
    ##### Synchronize and read frame
    received, flipped = findFrameStart()
    frameCorrect = False
    frameNumber = -1
    frame = ""
    if(received):
        binFrame = readPayload(flipped)
        frameCorrect, binFrame = checkFrame(binFrame)
        frame = decode_binary_string(binFrame[PACKETNUMLENGHT:])
        frameNumber = int(binFrame[:PACKETNUMLENGHT], 2)

        return True, frameCorrect, frameNumber, frame
    else:
        return False, frameCorrect, frameNumber, frame


