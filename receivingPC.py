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
startTime = time.time()




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
        "Correct=" + str(correct),
        "Duration=" + str(int(time.time() - startTime))
    )
    print(output.keys())




###### Read frames while frames are not all received ######
while(len(output) < totalPackets - 2 and time.time() - startTime < TESTTIME):
    count+= 1
    received, frameCorrect, frameNumber, frame = receive.readFrame()

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


