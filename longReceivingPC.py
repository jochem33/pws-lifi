from os import sync
import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time

from constants import *


from testvalues import *



rx = serial.Serial(RECEIVINGDEVICE,115201)



######## Wait till last 16 bits is the preamble, return if the bits are flipped or not #######
def findFrameStart():
    startTime = time.time()
    syncList = [2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2]
    while True:
        if (rx.inWaiting()>0):
            ##### Remove first item from synclist and append new bit
            del syncList[0]
            sData = rx.readline()
            bit = str(sData)[2]
            syncList.append(bit)

            ##### If framestart or reversed framestart is found, return true and if bits should be flipped
            if(syncList == FRAMESTART):
                return True, False
            if(syncList == ANTIFRAMESTART):
                return True, True

        ##### If timeout time has passed, return False for frame not found
        if(time.time() - startTime >= TIMEOUTTIME):
            return False, True



######## Read the payloadlenght + numberlenght bits and put them in payload string #######
def readPayload(flipped):
    payload = ""

    ##### Read payload while payload is not yet complete
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

        ##### Check frame, decode frame and parse framenumber
        frameCorrect, binFrame = checkFrame(binFrame)
        frame = decode_binary_string(binFrame[PACKETNUMLENGHT:])
        frameNumber = int(binFrame[:PACKETNUMLENGHT], 2)

        return True, frameCorrect, frameNumber, frame
    else:
        return False, frameCorrect, frameNumber, frame









######## Print progressdata and succesrate #######
def printDebugData(frameNumber, frame, count, totalPackets, output, correct):
    print("\n" * 30)
    print("___________ Frame " + str(frameNumber) + " ___________")
    print(frame)
    print("Count=" + str(count),
    #  "Correct=" + str(correctCount),
    #   "Percentage=" + str(int(correctCount/count *100)) + "%",
       "Total=" + str(totalPackets),
        "Received=" + str(len(output)),
        "Correct=" + str(correct),
        "Duration=" + str(int(time.time() - startTime))
    )
    print(output.keys())





def main():
    ###### Var setup for data reading loop ######
    count = 0
    correctCount = 0
    totalPackets = 35000
    output = {}
    startTime = time.time()

    ###### Read frames while frames are not all received ######
    while(len(output) < totalPackets - 2 and time.time() - startTime < TESTTIME):
        count+= 1
        received, frameCorrect, frameNumber, frame = readFrame()

        if(received):
            ##### Validate frame, if correct, use frame, else, send reset signal to arduino
            if(frameCorrect):
                correctCount+= 1
                ##### if num=0 use frame as header, else add to output list
                if(int(frameNumber) == 0):
                    totalPackets = int(frame[:8])
                else:
                    output[frameNumber - 1] = frame
            else:
                ##### Send reset signal to arduino
                rx.write(bytes("0", encoding='utf-8'))
            ##### Print debugging data
            printDebugData(frameNumber, frame, count, totalPackets, output, frameCorrect)
        else:
            count-= 1
            print("Not received")
        #     send.sendFrame("YESS" + (PAYLOADLENGHT - PARITYLENGHT) * "b", 9999)
            
        


    ###### Concattinate outputs list into string ######
    # outputString = ""
    # for i in range(len(output)):
    #     outputString = outputString + output[i]



    # ###### Write output to outputfile ######
    # f = open(OUTPUTFILE, "w")
    # f.write(outputString)
    # f.close()



    ###### Write report ######
    f = open("results.csv", "a")
    f.write("\n")
    f.write(str(GAPLENGHT) + ",    ")
    f.write(str(PREAMBLELENGHT) + ",    ")
    f.write(str(PAYLOADLENGHT) + ",    ")
    f.write(str(DATARATE) + ",    ")
    f.write(str(int(1/DATARATE)) + "b/s" + ",    ")
    f.write(str(totalPackets) + ",    ")
    f.write(str(totalPackets * TOTALLENGHT) + ",    ")


    f.write(str(count) + ",    ")
    f.write(str(correctCount) + ",    ")
    f.write(str(int(correctCount/count *100)) + "%" + ",    ")

    f.write(str(startTime) + ",    ")
    f.write(str(time.time()) + ",    ")
    f.write(str(time.time() - startTime) + ",    ")
    f.write(str(int(count - (time.time() - startTime) / TOTALLENGHT)) + ",    ")
    f.write(str(int(correctCount * TOTALLENGHT / (time.time() - startTime))) + ",    ")
    f.write(str(int(correctCount * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))) + ",    ")
    f.write(str(int(len(output) * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))) + ",    ")
    f.write(str(DISTANCE))

    f.close()




    ###### Print report ######
    print("__________ Run at " + str(startTime) + " __________")
    print("GAPLENGHT: " + str(GAPLENGHT))
    print("PREAMBLELENGHT: " + str(PREAMBLELENGHT))
    print("PAYLOADLENGHT: " + str(PAYLOADLENGHT))
    print("DATARATE: " + str(DATARATE))
    print("speed: " + str(int(1/DATARATE)) + "b/s")
    print("totalPackets: " + str(totalPackets))
    print("totalBits: " + str(totalPackets * TOTALLENGHT))


    print("Count: " + str(count))
    print("correctCount: " + str(correctCount))
    print("correctPercentage=" + str(int(correctCount/count *100)) + "%")

    print("Starttime: " + str(startTime))
    print("Endtime: " + str(time.time()))
    print("Duration: " + str(time.time() - startTime))
    print("Missedframes: " + str(int(count - (time.time() - startTime) / TOTALLENGHT)))
    print("correctDataSpeed: " + str(int(correctCount * TOTALLENGHT / (time.time() - startTime))))
    print("correctPayloadSpeed: " + str(int(correctCount * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))))
    print("usefullPayloadSpeed: " + str(int(len(output) * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))))







for i in range(len(testValues)):
    
    startTime = time.time()




    GAPLENGHT = testValues[i]["GAPLENGHT"]
    PREAMBLELENGHT = testValues[i]["PREAMBLELENGHT"]
    PACKETNUMLENGHT = testValues[i]["PACKETNUMLENGHT"]
    PARITYLENGHT = testValues[i]["PARITYLENGHT"]
    PAYLOADLENGHT = testValues[i]["PAYLOADLENGHT"]
    TOTALLENGHT = GAPLENGHT + PREAMBLELENGHT + PACKETNUMLENGHT + PAYLOADLENGHT
    TIMEOUTTIME = testValues[i]["TIMEOUTTIME"]
    TESTTIME = testValues[i]["TESTTIME"]

    main()