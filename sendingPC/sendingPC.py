import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time
import math


######## const setup ######
DATARATE = 0.005
GAPLENGHT = 24
PREAMBLELENGHT = 24
PACKETNUMLENGHT = 16
PAYLOADLENGHT = 256
ENDOFFRAMELENGHT = 8
############################



######## serial setup ######
ser = serial.Serial('/dev/cu.usbserial-14110', 115201, timeout=1)
############################



######## data setup ######
print("___________ Reading File ___________")

# read file
inputFile = open('input.html', 'r') 
fileContent = inputFile.read()
inputFile.close()

#convert to binary
binFile = "".join(f"{ord(i):08b}" for i in fileContent)
binFile = binFile.replace(" ", "")
############################



######## time setup #######
currentTime = time.time()
previousTime = time.time()
############################



######## send nothing #######
def frameGap(i):
    if(i == 0):
        print("framegap")



######## send nothing #######
def preamble(i):
    if(i == 0):
        print("preamble")
    if(i < PREAMBLELENGHT - 1):
        ser.write(bytes("0", encoding='utf-8'))
    else:
        ser.write(bytes("1", encoding='utf-8'))



######## send packetnumber ####### 
###### this function may be removed because its the same as the 'payload' function
def packetNumber(i, bit):
    if(i == 0):
        print("packetnumber")
    currentByte = bytes(str(bit[i]), encoding='utf-8')
    ser.write(currentByte)



######## send payload #######
def payload(i, data):
    if(i == 0):
        print("payload")
    currentByte = bytes(str(data[i]), encoding='utf-8')
    ser.write(currentByte)
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


######## prep for main loop #######
packetcount = math.ceil(len(binFile) / PAYLOADLENGHT + 1)
print(packetcount)
packetindex = 0
############################



######## main loop #######
while True:
    if(packetindex != 0):
        payloaddata = binFile[(packetindex - 1) * PAYLOADLENGHT:(packetindex) * PAYLOADLENGHT]
    else:
        header = "HEADER__" + ((8 - len(str(int(packetcount)))) * "0") + str(packetcount) + (16 * "b")
        binHeader= "".join(f"{ord(i):08b}" for i in header)
        payloaddata = binHeader.replace(" ", "")

    packetIndex16bin = '{0:016b}'.format(packetindex)
    print("___________ Frame " + str(packetindex) + "/" + str(packetcount) + " ___________")
    print(packetIndex16bin)

    ###### every phase of the entire frame
    repeatInterval(frameGap, GAPLENGHT)
    repeatInterval(preamble, PREAMBLELENGHT)
    repeatInterval(packetNumber, PACKETNUMLENGHT, packetIndex16bin)
    repeatInterval(payload, PAYLOADLENGHT, payloaddata)
        

    packetindex = packetindex + 1
    if(packetindex >= packetcount - 1):
        packetindex = 0
        
