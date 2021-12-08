from os import sync
import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time

from constants import *
import receive
import send

rx = serial.Serial(RECEIVINGDEVICE,115201)

###### Var setup for data reading loop ######
count = 0
correctCount = 0
totalPackets = 35000
output = {}




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




###### Read frames while frames are not all received ######
while len(output) < totalPackets - 2:
    count+= 1

    received, frameCorrect, frameNumber, frame = receive.readFrame()

    if(received):
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
            rx.write(bytes("0", encoding='utf-8'))
    else:
        send.sendFrame("")
        
    ##### Print debugging data
    printDebugData(frameNumber, frame, count, totalPackets, output, frameCorrect)
    


###### Concattinate outputs list into string ######
outputString = ""
for i in range(len(output)):
    outputString = outputString + output[i]



###### Write output to outputfile ######
f = open(OUTPUTFILE, "w")
f.write(outputString)
f.close()