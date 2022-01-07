import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time
import math

from constants import *

from testvalues import *


######## serial setup ######
tx = serial.Serial(SENDINGDEVICE, BAUDRATE, timeout=1)
############################





startTime = time.time()




######## data setup ######
print("___________ Reading File ___________")

# read file
inputFile = open(INPUTFILE, 'r') 
fileContent = inputFile.read()
inputFile.close()
fileContent = fileContent + (" " * int(PAYLOADLENGHT / 8))
############################



######## prep for main loop #######
PACKETCOUNT = math.ceil(len(fileContent * 8) / (PAYLOADLENGHT - PARITYLENGHT) + 1)
frameIndex = 0
############################




######## time setup #######
currentTime = time.time()
previousTime = time.time()
############################



######## send nothing #######
def frameGap(i):
    if(i == 0):
        print("framegap")



######## send 0's and one 1 #######
def preamble(i):
    if(i == 0):
        print("preamble")
    if(i < PREAMBLELENGHT - 2):
        tx.write(bytes(str((i+1)%2), encoding='utf-8'))
    else:
        tx.write(bytes("1", encoding='utf-8'))



######## send packetnumber ####### 
###### this function may be removed because its the same as the 'payload' function
def packetNumber(i, bit):
    if(i == 0):
        print("packetnumber")
    currentByte = bytes(str(bit[i]), encoding='utf-8')
    tx.write(currentByte)



######## send payload #######
def payload(i, data):
    if(i == 0):
        print("payload")
    currentByte = bytes(str(data[i]), encoding='utf-8')
    tx.write(currentByte)
    print(str(currentByte)[2], end="")
    if(i == PAYLOADLENGHT - 1):
        print("")



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
    
    ##### Add parity
    paritycount = len(payloaddata.replace("0", ""))
    binparitycount = '{0:016b}'.format(paritycount)
    payloaddata = payloaddata + ((PARITYLENGHT - len(str(binparitycount))) * "0") + binparitycount

    ##### Make binary frameIndex
    frameIndex16bin = '{0:016b}'.format(frameIndex)

    ###### every phase of the entire frame
    repeatInterval(frameGap, GAPLENGHT)
    repeatInterval(preamble, PREAMBLELENGHT)
    repeatInterval(packetNumber, PACKETNUMLENGHT, frameIndex16bin)
    repeatInterval(payload, PAYLOADLENGHT, payloaddata)





######## main loop #######
def main():
    frameIndex = 0
    while time.time() - startTime < TESTTIME:
        payload = ""
        ##### Grab payload from file or make the header
        if(frameIndex != 0):
            payload = fileContent[(frameIndex - 1) * (int(PAYLOADLENGHT / 8) - int(PARITYLENGHT / 8)):(frameIndex) * (int(PAYLOADLENGHT / 8) - int(PARITYLENGHT / 8))]
        else:
            payload = ((8 - len(str(int(PACKETCOUNT)))) * "0") + str(PACKETCOUNT) + "HEADER__" + (PAYLOADLENGHT * "b")


        ##### Send the frame
        sendFrame(payload, frameIndex)


        ##### Print debugging data
        print("___________ Frame " + str(frameIndex) + "/" + str(PACKETCOUNT) + " ___________")
        

        frameIndex = frameIndex + 1
        receivedAcknowledgement = False
        if(frameIndex >= PACKETCOUNT - 1):
            # while(receivedAcknowledgement != True):
            #     received, frameCorrect, frameNumber, frame = receive.readFrame()
            #     if(received and frameCorrect):
            #         print("Acknowledgement received")
            #         if(frame[:4] == "YESS"):
            #             receivedAcknowledgement = True
            frameIndex = 0






for i in range(len(testValues)):
    
    startTime = time.time()




    ######## data setup ######
    print("___________ Reading File ___________")

    # read file
    inputFile = open(INPUTFILE, 'r') 
    fileContent = inputFile.read()
    inputFile.close()
    fileContent = fileContent + (" " * int(PAYLOADLENGHT / 8))
    ############################



    ######## prep for main loop #######
    PACKETCOUNT = math.ceil(len(fileContent * 8) / (PAYLOADLENGHT - PARITYLENGHT) + 1)
    ############################

    GAPLENGHT = testValues[i]["GAPLENGHT"]
    PREAMBLELENGHT = testValues[i]["PREAMBLELENGHT"]
    PACKETNUMLENGHT = testValues[i]["PACKETNUMLENGHT"]
    PARITYLENGHT = testValues[i]["PARITYLENGHT"]
    PAYLOADLENGHT = testValues[i]["PAYLOADLENGHT"]
    TOTALLENGHT = GAPLENGHT + PREAMBLELENGHT + PACKETNUMLENGHT + PAYLOADLENGHT
    TIMEOUTTIME = testValues[i]["TIMEOUTTIME"]
    TESTTIME = testValues[i]["TESTTIME"]

    main()





