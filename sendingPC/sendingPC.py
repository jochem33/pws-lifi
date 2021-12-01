import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time

DATARATE = 0.005
GAPLENGHT = 24
PREAMBLELENGHT = 24
PAYLOADLENGHT = 64
ENDOFFRAMELENGHT = 8


######## serial setup ######
ser = serial.Serial('/dev/cu.usbserial-1410', 115201, timeout=1)
############################


######## data setup ######
print("___________ Reading File ___________")

# read file
inputFile = open('input.txt', 'r') 
fileContent = inputFile.read()
inputFile.close()

# add line ends and chunk numbers
#convert to binary
binFile = "".join(f"{ord(i):08b}" for i in fileContent)
binFile = binFile.replace(" ", "")

print(binFile)


######## time setup #######
currentTime = time.time()
previousTime = time.time()
############################

list = [0,1,0,0,0,0,0,1, 0,1,1,1,0,0,0,0, 0,1,1,1,0,0,0,0, 0,1,1,0,0,1,0,1, 0,1,1,0,1,1,0,0, 0,1,1,0,1,1,0,0, 0,1,1,0,0,1,0,1, 0,1,1,0,1,0,1,1]

def frameGap():
    previousTime = time.time()
    i = 0
    while i != GAPLENGHT:
        currentTime = time.time()
        if(currentTime - previousTime > DATARATE):
            previousTime = currentTime
            i+=1

def preamble():
    previousTime = time.time()
    i = 0
    while i != PREAMBLELENGHT:
        currentTime = time.time()
        if(currentTime - previousTime > DATARATE):
            previousTime = currentTime
            i+=1
            ser.write(bytes("0", encoding='utf-8'))
    ser.write(bytes("1", encoding='utf-8'))   


def payload(data):
    previousTime = time.time()
    i = 0
    while i != PAYLOADLENGHT:
        currentTime = time.time()

        if(currentTime - previousTime > DATARATE):
            previousTime = currentTime

            currentByte = bytes(str(data[i]), encoding='utf-8')
            ser.write(currentByte)
            print(currentByte)

            i+=1


while True:
    frameGap()
    preamble()
    payload(list)
        
