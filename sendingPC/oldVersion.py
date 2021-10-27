import warnings
import serial
import serial.tools.list_ports
from serial import Serial
import time


######## const and var setup ######
DATARATE = 0.02
chunkIndex = 0
dataIndex = 0
LINE_END_CHAR = "10100101"
LINE_END_CHAR_CHAR  = "¥"
writingLine = True
WHOLE_LINE_LENGHT = 16 * 8

###########################



######## data setup ######
print("___________ Reading File ___________")

# read file
file1 = open('input.txt', 'r') 
fileContent = file1.read()
file1.close()

# add line ends and chunk numbers
fileContentWithLineEndAndNumber = LINE_END_CHAR_CHAR  + (LINE_END_CHAR_CHAR  * 2).join(fileContent[i:i + 11]+ (3 - len(str(int(i/11)))) * "0" + str(int(i/11)) for i in range(0, len(fileContent), 11)) + LINE_END_CHAR_CHAR 

print(fileContentWithLineEndAndNumber)

#convert to binary
binFile = "".join(f"{ord(i):08b}" for i in fileContentWithLineEndAndNumber)
binFile = binFile.replace(" ", "")

print(binFile)

# split bin file in chunks
binChucksListWithLineEnd = [binFile[i:i+WHOLE_LINE_LENGHT] for i in range(0, len(binFile), WHOLE_LINE_LENGHT)]

dataLenght = len(binChucksListWithLineEnd)
##########################



######## serial setup ######
ser = serial.Serial('/dev/cu.usbserial-1420', 115201, timeout=1)
############################



######## time setup #######
currentTime = time.time()
previousTime = time.time()
############################


print("\n\n\n ___________ Starting ___________")

# main loop for sending data to serial
while True:
    while writingLine == True:
        currentTime = time.time()

        # check if enough time elapsed
        if(currentTime - previousTime > DATARATE):
            previousTime = currentTime

            # write byte to serial
            currentByte = bytes(binChucksListWithLineEnd[chunkIndex][dataIndex], encoding='utf-8')
            ser.write(currentByte)
            
            # print(binChucksListWithLineEnd[chunkIndex][dataIndex])
            dataIndex+= 1

            # if whole chunk is send
            if (dataIndex >= WHOLE_LINE_LENGHT):
                dataIndex = 0
                writingLine = False
    
    # go to next chunk
    writingLine = True
    chunkIndex+= 1

    #check if all chunks are send and restart
    if (chunkIndex >= dataLenght - 1):
        chunkIndex = 0
        print("\n___________ Restarting ___________")

