import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time
import math

from constants import *
# import receive
import send


######## serial setup ######
tx = serial.Serial(SENDINGDEVICE, BAUDRATE, timeout=1)
############################



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



######## main loop #######
while True:
    payload = ""
    ##### Grab payload from file or make the header
    if(frameIndex != 0):
        payload = fileContent[(frameIndex - 1) * (int(PAYLOADLENGHT / 8) - int(PARITYLENGHT / 8)):(frameIndex) * (int(PAYLOADLENGHT / 8) - int(PARITYLENGHT / 8))]
    else:
        payload = "HEADER__" + ((8 - len(str(int(PACKETCOUNT)))) * "0") + str(PACKETCOUNT) + (15 * "b")

    send.sendFrame(payload, frameIndex)
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
        
