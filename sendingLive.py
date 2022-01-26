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



######## main loop #######
def sendData(textData):
    PACKETCOUNT = math.ceil(len(textData * 8) / (PAYLOADLENGHT - PARITYLENGHT) + 1)
    frameIndex = 0
    for i in range(PACKETCOUNT * 5):
        payload = ""
        ##### Grab payload from text or make the header
        if(frameIndex != 0):
            payload = textData[(frameIndex - 1) * (int(PAYLOADLENGHT / 8) - int(PARITYLENGHT / 8)):(frameIndex) * (int(PAYLOADLENGHT / 8) - int(PARITYLENGHT / 8))]
        else:
            payload = ((8 - len(str(int(PACKETCOUNT)))) * "0") + str(PACKETCOUNT) + "HEADER__" + PAYLOADLENGHT * "b"
            payload = payload[0:int((PAYLOADLENGHT - PARITYLENGHT) / 8)]

        ##### Send the frame
        send.sendFrame(payload, frameIndex)


        ##### Print debugging data
        # print("___________ Frame " + str(frameIndex) + "/" + str(PACKETCOUNT) + " ___________")
        

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
        

while True:
    text = input("> ")
    text = text + int(((PAYLOADLENGHT - PARITYLENGHT) - len(text)%(PAYLOADLENGHT - PARITYLENGHT)) / 8) * " "
    sendData(text)
    