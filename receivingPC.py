# from os import sync
# import warnings

import serial
import serial.tools.list_ports
from serial import Serial
import time

from constants import *
import printDebugData

import receive
# import send

rx = serial.Serial(RECEIVINGDEVICE,BAUDRATE)

###### Var setup for data reading loop ######
count = 0
correctCount = 0
totalPackets = 3500000
tempTotalPackets = 0
output = {}
startTime = time.time()



    




###### Read frames while frames are not all received ######
while(len(output) < totalPackets - 1):
    count+= 1
    received, frameCorrect, frameNumber, frame = receive.readFrame()

    if(received):
        if(frameNumber == 0):
            print("HEADER FRAME")
            try:
                totalPackets = int(frame[:8])
            except:
                print("incorrect frame")
        ##### Validate frame, if correct, use frame, else, send reset signal to arduino
        else: 
            if(frameCorrect):
                correctCount+= 1
                ##### if num=0 use frame as header, else add to output list
                
                output[frameNumber - 1] = frame
        ##### Print debugging data
        tempTotalPackets = printDebugData.send(frameNumber, frame, count, totalPackets, output, frameCorrect, tempTotalPackets, correctCount, startTime)
    else:
        count-= 1
        print("Not received")
    #     send.sendFrame("YESS" + (PAYLOADLENGHT - PARITYLENGHT) * "b", 9999)
        
printDebugData.printReport(frameNumber, frame, count, totalPackets, output, frameCorrect, tempTotalPackets, correctCount, startTime) 

##### Concattinate outputs list into string ######
outputString = ""
for i in range(len(output) - 1):
    outputString = outputString + output[i]



###### Write output to outputfile ######
f = open(OUTPUTFILE, "w")
f.write(outputString)
f.close()

