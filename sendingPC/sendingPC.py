import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time



######## const setup ######
DATARATE = 0.005
GAPLENGHT = 24
PREAMBLELENGHT = 24
PACKETNUMLENGHT = 16
PAYLOADLENGHT = 256
ENDOFFRAMELENGHT = 8
############################



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
############################



######## time setup #######
currentTime = time.time()
previousTime = time.time()
############################



######## send nothing #######
def frameGap(i):
    print("framegap")



######## send nothing #######
def preamble(i):
    if(i < PREAMBLELENGHT - 1):
        print("Preamble 0")
        ser.write(bytes("0", encoding='utf-8'))
    else:
        print("Preamble 1")
        ser.write(bytes("1", encoding='utf-8'))



######## send packetnumber ####### 
###### this function may be removed because its the same as the 'payload' function
def packetNumber(i, packetindex):
    currentByte = bytes(str(packetindex), encoding='utf-8')
    ser.write(currentByte)
    print(currentByte)



######## send payload #######
def payload(i, data):
    currentByte = bytes(str(data[i]), encoding='utf-8')
    ser.write(currentByte)
    print(currentByte)



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
packetcount = len(binFile) / PAYLOADLENGHT
print(packetcount)
packetindex = 0
############################



######## main loop #######
while True:
    payloaddata = binFile[packetindex * PAYLOADLENGHT:(packetindex + 1) * PAYLOADLENGHT]
    ###### code for creating packetnumbers goes here (bin = '{0:016b}'.format(val))

    ###### every phase of the entire frame
    repeatInterval(frameGap, GAPLENGHT)
    repeatInterval(preamble, PREAMBLELENGHT)
    # repeatInterval(packetNumber, PACKETNUMLENGHT, packetindex)
    repeatInterval(payload, PAYLOADLENGHT, payloaddata)


    packetindex = packetindex + 1
    if(packetindex >= packetcount - 1):
        packetindex = 0
        
