from os import sync
import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time


FRAMESIZE = 256
PACKETNUMLENGHT = 16

# DATARATE = 0.24
currentTime = time.time()
previousTime = time.time()

FRAMASTART = ["0","0","0","0","0","0","0","0", "0","0","0","0","0","0","0","1"]
ANTIFRAMASTART = ["1","1","1","1","1","1","1","1", "1","1","1","1","1","1","1","0"]


sPort = '/dev/cu.usbmodem141201'

ser = serial.Serial(sPort,115201)

receiving = False


        
def findFrameStart():
    # print("Syncdata: ")
    unSynced = True
    syncList = [2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2]
    while unSynced:
        if (ser.inWaiting()>0):
            del syncList[0]
            sData = ser.readline()
            bit = str(sData)[2]
            # print(bit, end="")
            syncList.append(bit)
            if(syncList == FRAMASTART):
                # print("\nFound, normal")
                return False
            if(syncList == ANTIFRAMASTART):
                # print("\nFound, flipped")
                return True

        
def readFrame(flipped):
    payload = ""
    while len(payload) < FRAMESIZE + PACKETNUMLENGHT:
        if (ser.inWaiting()>0):

            sData = ser.readline()
            bit = str(sData)[2]
            if(flipped):
                bit = int(bit) * -1 + 1
            payload = payload + str(bit)
    return payload


def readFrameNum(flipped):
    binNumber = ""
    while len(binNumber) < PACKETNUMLENGHT:
        if (ser.inWaiting()>0):

            sData = ser.readline()
            bit = str(sData)[2]
            if(flipped):
                bit = int(bit) * -1 + 1
            binNumber = binNumber + str(bit)
    return binNumber

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


count = 0
correct = 0
totalPackets = 35000
output = {}
while len(output) < totalPackets - 2:
    count+= 1
    flipped = findFrameStart()

    binFrame = readFrame(flipped)
    frame = decode_binary_string(binFrame[16:])
    frameNumber = int(binFrame[:16], 2)
    if(frameNumber < 200):
        correct+= 1
        if(frameNumber == 0):
            if(frame[8:16].isnumeric()):
                print(frame[8:16])
                totalPackets = int(frame[8:16])
        else:
            output[frameNumber - 1] = frame
    else:
        print("RESET")
        ser.write(bytes("0", encoding='utf-8'))

    print("\n" * 30)
    print("___________ Frame " + str(frameNumber - 1) + " ___________")
    print(frame)
    print("Count=" + str(count), "Correct=" + str(correct), "Percentage=" + str(int(correct/count *100)) + "%", "Total=" + str(totalPackets), "Received=" + str(len(output)))
    print(output.keys())


outputString = ""
for i in range(len(output)):
    outputString = outputString + output[i]
print(outputString)

path = 'output.html'

f = open(path, "w")
f.write(outputString)
f.close()