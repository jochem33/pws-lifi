import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time

DATARATE = 0.005
GAPLENGHT = 24
PREAMBLELENGHT = 24
PACKETNUMLENGHT = 16
PAYLOADLENGHT = 256
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

#convert to binary
binFile = "".join(f"{ord(i):08b}" for i in fileContent)
binFile = binFile.replace(" ", "")

print(binFile)


######## time setup #######
currentTime = time.time()
previousTime = time.time()
############################


def frameGap(i):
    print("framegap")

def preamble(i):
    if(i < PREAMBLELENGHT - 1):
        print("Preamble 0")
        ser.write(bytes("0", encoding='utf-8'))
    else:
        print("Preamble 1")
        ser.write(bytes("1", encoding='utf-8'))


def packetNumber(i, packetindex):
    currentByte = bytes(str(packetindex), encoding='utf-8')
    ser.write(currentByte)
    print(currentByte)


def payload(i, data):
    currentByte = bytes(str(data[i]), encoding='utf-8')
    ser.write(currentByte)
    print(currentByte)


def repeatInterval(callback, count, arg=None):
    previousTime = time.time()
    i = 0
    while i < count:
        currentTime = time.time()

        if(currentTime - previousTime > DATARATE):
            previousTime = currentTime

            if(arg is not None):
                callback(i, arg)
            else:
                callback(i)
            i+=1


packetcount = len(binFile) / PAYLOADLENGHT
print(packetcount)
packetindex = 0
while True:
    repeatInterval(frameGap, GAPLENGHT)
    repeatInterval(preamble, PREAMBLELENGHT)
    # repeatInterval(packetNumber, PACKETNUMLENGHT, packetindex)
    payloaddata = binFile[packetindex * PAYLOADLENGHT:(packetindex + 1) * PAYLOADLENGHT]
    # print(payloaddata, ((packetindex + 1)))
    repeatInterval(payload, PAYLOADLENGHT, payloaddata)
    packetindex = packetindex + 1
    if(packetindex >= packetcount - 1):
        packetindex = 0
        
