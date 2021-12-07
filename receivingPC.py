from os import sync
import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time
from constants import *

ser = serial.Serial(RECEIVINGDEVICE,115201)


###### Var setup for data reading loop ######
count = 0
correctCount = 0
totalPackets = 35000
output = {}



######## Wait till last 16 bits is the preamble, return if the bits are flipped or not #######
def findFrameStart():
    unSynced = True
    syncList = [2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2]
    while unSynced:
        if (ser.inWaiting()>0):
            del syncList[0]
            sData = ser.readline()
            bit = str(sData)[2]
            syncList.append(bit)
            if(syncList == FRAMESTART):
                return False
            if(syncList == ANTIFRAMESTART):
                return True



######## Read the payloadlenght + numberlenght bits and put them in payload string #######
def readPayload(flipped):
    payload = ""
    while len(payload) < PAYLOADLENGHT + PACKETNUMLENGHT:
        if (ser.inWaiting()>0):

            sData = ser.readline()
            bit = str(sData)[2]
            if(flipped):
                bit = int(bit) * -1 + 1
            payload = payload + str(bit)
    return payload



######## Translate binary string and return payload in text #######
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))




######## Print progressdata and succesrate #######
def printDebugData(frameNumber, frame, count, totalPackets, output, correct):
    print("\n" * 30)
    print("___________ Frame " + str(frameNumber) + " ___________")
    print(frame)
    print("Count=" + str(count),
     "Correct=" + str(correctCount),
      "Percentage=" + str(int(correctCount/count *100)) + "%",
       "Total=" + str(totalPackets),
        "Received=" + str(len(output)),
        "Correct=" + str(correct)
    )
    print(output.keys())



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
    flipped = findFrameStart()
    binFrame = readPayload(flipped)
    frameCorrect, binFrame = checkFrame(binFrame)
    frame = decode_binary_string(binFrame[PACKETNUMLENGHT:])
    frameNumber = int(binFrame[:PACKETNUMLENGHT], 2)

    

    ##### Print debugging data
    printDebugData(frameNumber, frame, count, totalPackets, output, frameCorrect)
    return frameCorrect, frameNumber, frame





###### Read frames while frames are not all received ######
while len(output) < totalPackets - 2:
    count+= 1

    frameCorrect, frameNumber, frame = readFrame()

    ##### Validate frame, if correct, use frame, else, send reset signal to arduino
    if(frameCorrect):
        correctCount+= 1
        ##### if num=0 use frame as header, else add to output list
        if(int(frameNumber) == 0):
            # if(frame[8:16].isnumeric()):
            totalPackets = int(frame[8:16])
        else:
            output[frameNumber - 1] = frame
    else:
        ser.write(bytes("0", encoding='utf-8'))

    


###### Concattinate outputs list into string ######
outputString = ""
for i in range(len(output)):
    outputString = outputString + output[i]



###### Write output to outputfile ######
f = open(OUTPUTFILE, "w")
f.write(outputString)
f.close()