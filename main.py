from gettext import find
import sys
import threading
from constants import *
import serial

import printDebugData

import receive
import send


deviceNum = int(sys.argv[1])

startState = "WAIT"
if(deviceNum == 0):
    startState = "SEND"
    dev = serial.Serial(SENDINGDEVICE,BAUDRATE)
else:
    dev = serial.Serial(RECEIVINGDEVICE,BAUDRATE)


state = startState
receiveState = "FIND"
sendType = "" # FILETRANSMIT REQUEST RETRANSMIT 
sendState = ""

sendingFile = ""
sendingFrame = 0

fileDir = {}

allComplete = False
userinput = False

while True:
    print(state, receiveState)
    if(state == "WAIT"):
        if(dev.inWaiting()>0):
            state = "RECEIVE"
            receiveState = "FIND"
        # elif(not dev.inWaiting()>0 and not allComplete):
        #     state = "SEND"
        #     sendType = "REQUEST"
        elif(userinput):
            state = "SEND"


    if(state == "RECEIVE"):
        frameType = ""
        fileNum = -1
        frameNum = -1
        payload = ""
        correctedPayload = ""
        frameCorrect = False

        if(receiveState == "FIND"):
            if(receive.findFrameStart(dev)):
                receiveState = "TYPE"
            else:
                state = "WAIT"

        if(receiveState == "TYPE"):
            frameType = receive.read(TYPELENGHT, dev)
            receiveState = "FILENUM"

        if(receiveState == "FILENUM"):
            fileNum = receive.read(FILENUMLENGTH, dev)
            receiveState = "FRAMENUM"

        if(receiveState == "FRAMENUM"):
            frameNum = receive.read(FRAMENUMLENGHT, dev)
            receiveState = "PAYLOAD"

        if(receiveState == "PAYLOAD"):
            payload = receive.read(PAYLOADLENGHT, dev)
            receiveState = "VALIDATE"

        
        if(receiveState == "VALIDATE"):
            frameCorrect, correctedPayload = receive.checkFrame(payload)
            print(fileNum, frameNum, frameCorrect, payload[:8])
            if(frameCorrect):
                fileDir[fileNum]["frames"][frameNum] = payload
                if(len(fileDir[fileNum].frames) >= fileDir[fileNum].totalFrames):
                    state = "WAIT"
            receiveState = "FIND"

        # printDebugData.receiveStatus2(frame, state, fileDir[frame.filenum])



    if(state == "SEND"):
        # if(sendType):


        if(sendState == "GAP"):
            send.repeatInterval(send.frameGap, GAPLENGHT)
            sendState = "PREAMBLE"

        if(sendState == "PREAMBLE"):
            send.repeatInterval(send.preamble, PREAMBLELENGHT)
            sendState = "TYPE"

        if(sendState == "TYPE"):
            while not allSend:
                send
            sendState = "FILENUM"

        if(sendState == "FILENUM"):
            while not allSend:
                send
            sendState = "FRAMENUM"

        if(sendState == "FRAMENUM"):
            while not allSend:
                send
            sendState = "PAYLOAD"

        if(sendState == "PAYLOAD"):
            while not allSend:
                send
            if(not ALLSEND)
                sendingFrame+=1
                sendState = "GAP"
            else:
                sendingFrame = 0
                sendingFile = ""
                sendState = "GAP"
                state = "WAIT"