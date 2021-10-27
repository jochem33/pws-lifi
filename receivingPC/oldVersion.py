import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import webbrowser
import os


######## const setup ######
FILENAME = 'output.html'
LINE_END_CHAR = ['1', '0', '1', '0', '0', '1', '0', '1']
LINE_END_CHAR_CHAR = "¥"
sPort = '/dev/cu.usbmodem142101'
###########################



######## var setup ######
file1 = open(FILENAME, 'w+') 
file1.write("") 
file1.close() 


aSerialData = serial.Serial(sPort,115201)

character = []

text = [""]
receiving = True

receivedChunks = {}

debugData = {"Synchronising": "NO",
            "syncTime":0,
            "text":"",
            "chunkValid":"",
            "newChunk":"NO"
            }
###########################



######## printing all debuging information ######
def printDebugData():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Synchronising: ", debugData["Synchronising"])
    print("syncTime: ", debugData["syncTime"])
    print("Received chunks: (", len(receivedChunks.keys()), ") ", receivedChunks.keys())
    print("Chunk valid: ", debugData["chunkValid"])
    print("New chunk: ", debugData["newChunk"])
    print("\n_________________________")
    print("Current chunk: ", debugData["text"])
    print("\n_________________________")
    print(str(receivedChunks).replace(",", "\n"))
###########################


######## function that looks for a syncchar in datastream ######
def synchronize(syncChar):
    debugData["Synchronising"] = "YES"

    # reset sync vars
    syncList = []
    synced = False
    syncTime = 0

    #start syncing
    while synced == False:
        #if bit is found
        if (aSerialData.inWaiting()>0):
            # start timing
            debugData["syncTime"] = syncTime
            printDebugData()
            syncTime+=1
            debugData["syncTime"] = syncTime

            #add bit to synclist
            sData = aSerialData.readline()
            bit = str(sData)[2]
            syncList.append(bit)

            #if synclist contains line end char, stop syncing
            if(syncList[-8:] == syncChar and synced == False):
                if(syncList[-16:-8] == syncChar):
                    text = [LINE_END_CHAR_CHAR]
                    print("Double syncchar!!!")
                else:
                    text = []
                debugData["Synchronising"] = "NO"
                synced = True
###########################


######## function that checks if all chunks came in ######
def integretyCheck(lastLineNum):
    if(len(receivedChunks) >= lastLineNum):
        print("integretycheck excellent")
        return(True)
    else:
        return(False)
###########################



# first synchronisation
print("Waiting for signal...\n")
synchronize(LINE_END_CHAR)


# main loop
while receiving:
    # if serial data is found
    if (aSerialData.inWaiting()>0):

        # get bits and put them in character list
        sData = aSerialData.readline()
        bit = str(sData)[2]
        character.append(bit)

        # if 8 bits in character list
        if (len(character) == 8):
            #convert from binary to letter
            letter = chr(int("".join(character), 2))
            text.append(letter)
            character = []

            #update debug data
            debugData["text"] = "".join(text).replace("¥", "=")
            printDebugData()

            # check if string starts with line end character
            if not(text[0] == LINE_END_CHAR_CHAR):
                text = []
                synchronize(LINE_END_CHAR)

        # if 16 characters are received
        if (len(text) >= 16):
            textStr = ""
            textStr = textStr.join(text)

            # if chunk starts and ends with the line end character
            if(textStr[0] == LINE_END_CHAR_CHAR and textStr[-0] == LINE_END_CHAR_CHAR):
                lineNum = textStr[12:15]

                # try if the last part of the chunk is a number
                try:
                    lineNum = int(lineNum)
                    lineValid = True
                    debugData["chunkValid"] = "YES"
                except ValueError:
                    debugData["chunkValid"] = "NO"
                    lineValid = False
                    synchronize(LINE_END_CHAR)
                
                # if chunk is ok
                if(lineValid):
                    # if chunk is not yet known, add it to the list, else do nothing
                    if not(lineNum in receivedChunks):
                        debugData["newChunk"] = "YES"
                        receivedChunks[lineNum] = textStr[1:-4]
                    else:
                            debugData["newChunk"] = "NO"

                    # if the end character is found in the chunk
                    if("END" in textStr):
                        print("____ END ____", lineNum)
                        
                        #check if all lines are received
                        integrety = integretyCheck(lineNum)

                        if(integrety):
                            # stick final file together
                            finalFile = []
                            for i in range(lineNum):
                                finalFile.append(receivedChunks.get(i, ""))

                            # put content in output file
                            file1 = open(FILENAME, 'a') 
                            file1.write(''.join(finalFile))
                            file1.close() 

                            # end main loop
                            receiving = False

                            # open output in webbrowser
                            webbrowser.open('file://' + os.path.realpath(FILENAME))

            # if the chunk is not correct, synchronise    
            else:
                synchronize(LINE_END_CHAR)
            if not(text == [LINE_END_CHAR_CHAR]):
                text = []


