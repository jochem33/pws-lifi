# from os import sync
# import warnings
import math

import serial
import serial.tools.list_ports
from serial import Serial
import time

from constants import *
import receive
# import send

rx = serial.Serial(RECEIVINGDEVICE,BAUDRATE)

###### Var setup for data reading loop ######
count = 0
correctCount = 0
totalPackets = 35000
output = {}
startTime = time.time()


terminalWidth = 70

######## Print text in a line with hashtags #######
def formatString(text):
    print("# " + text + " "* (terminalWidth - len(text) - 4) + " #")


######## Print progressdata and succesrate #######
def printDebugData(frameNumber, frame, count, totalPackets, output, correct):
    # print("\n" * 30)
    # print("___________ Frame " + str(frameNumber) + " ___________")
    # print(frame)
    # print("Count=" + str(count),
    #  "Correct=" + str(correctCount),
    #   "Percentage=" + str(int(correctCount/count *100)) + "%",
    #    "Total=" + str(totalPackets),
    #     "Received=" + str(len(output)),
    #     "Correct=" + str(correct),
    #     "Duration=" + str(int(time.time() - startTime))
    # )
    # print(output.keys())

    
    frameSymbolSting = ""
    if(totalPackets < 35000):
        for i in range(totalPackets):
            if(i == frameNumber):
                frameSymbolSting = frameSymbolSting + ">"
            else:
                frameSymbolSting = frameSymbolSting + " "
            if(i + 1 not in output):
                frameSymbolSting = frameSymbolSting + "◻"
            else:
                frameSymbolSting = frameSymbolSting + "◼"

    print(30 * "\n")
    print("#" * terminalWidth)
    formatString("")
    formatString(" Received frames")

    for i in range(math.ceil(len(frameSymbolSting) / 40)):
        formatString(frameSymbolSting[i*40:(i+1)*40])

    formatString("")
    formatString(frame)
    formatString("")
    formatString("totalFrames=" + str(totalPackets))
    formatString("receivedFrames=" + str(len(output)))
    formatString("receivedCorrectFrames=" + str(correctCount))
    formatString("correctPercentage=" + str(int(correctCount/count *100)) + "%")
    formatString("currentCorrect=" + str(correct))
    formatString("duration=" + str(int(time.time() - startTime)) + "s")
    formatString("")

    print("#" * terminalWidth)
    print()

    




###### Read frames while frames are not all received ######
while(len(output) < totalPackets - 2):
    count+= 1
    received, frameCorrect, frameNumber, frame = receive.readFrame()

    if(received):
        if(frameNumber == 0):
            print("HEADER FRAME")
            totalPackets = int(frame[:8])
        ##### Validate frame, if correct, use frame, else, send reset signal to arduino
        else: 
            if(frameCorrect):
                correctCount+= 1
                ##### if num=0 use frame as header, else add to output list
                
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
        
    


##### Concattinate outputs list into string ######
outputString = ""
for i in range(len(output)):
    outputString = outputString + output[i]



###### Write output to outputfile ######
f = open(OUTPUTFILE, "w")
f.write(outputString)
f.close()



# ###### Write report ######
# f = open("results.csv", "a")
# f.write("\n")
# f.write(str(GAPLENGHT) + ",    ")
# f.write(str(PREAMBLELENGHT) + ",    ")
# f.write(str(PAYLOADLENGHT) + ",    ")
# f.write(str(DATARATE) + ",    ")
# f.write(str(int(1/DATARATE)) + "b/s" + ",    ")
# f.write(str(totalPackets) + ",    ")
# f.write(str(totalPackets * TOTALLENGHT) + ",    ")


# f.write(str(count) + ",    ")
# f.write(str(correctCount) + ",    ")
# f.write(str(int(correctCount/count *100)) + "%" + ",    ")

# f.write(str(startTime) + ",    ")
# f.write(str(time.time()) + ",    ")
# f.write(str(time.time() - startTime) + ",    ")
# f.write(str(int(count - (time.time() - startTime) / TOTALLENGHT)) + ",    ")
# f.write(str(int(correctCount * TOTALLENGHT / (time.time() - startTime))) + ",    ")
# f.write(str(int(correctCount * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))) + ",    ")
# f.write(str(int(len(output) * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))) + ",    ")
# f.write(str(DISTANCE))

# f.close()




###### Print report ######
print("__________ Run at " + str(startTime) + " __________")
print("GAPLENGHT: " + str(GAPLENGHT))
print("PREAMBLELENGHT: " + str(PREAMBLELENGHT))
print("PAYLOADLENGHT: " + str(PAYLOADLENGHT))
print("DATARATE: " + str(DATARATE))
print("frequency: " + str(int(1/DATARATE)) + "b/s")
print("totalPackets: " + str(totalPackets))
print("totalBits: " + str(totalPackets * TOTALLENGHT))
print()

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
print()
print("Transferspeed: " + str(int(len(output) * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))) + "b/s")

print("\n\n")
print(outputString)