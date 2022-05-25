from constants import *
import math
import time

######## Print text in a line with hashtags #######
def formatString(text):
    print("# " + text + " "* (TERMINALWIDTH - len(text) - 4) + " #")


######## Print progressdata and succesrate #######
def send(frameNumber, frame, count, totalPackets, output, correct, tempTotalPackets, correctCount, startTime):

    if(frameNumber > tempTotalPackets and correct):
        tempTotalPackets = frameNumber

    if(totalPackets != 3500000):
        tempTotalPackets = totalPackets
    
    frameSymbolSting = ""
    if(tempTotalPackets < 3500000):
        for i in range(tempTotalPackets):
            if(i == frameNumber):
                frameSymbolSting = frameSymbolSting + ">"
            else:
                frameSymbolSting = frameSymbolSting + " "
            if(i + 1 not in output):
                frameSymbolSting = frameSymbolSting + "◻"
            else:
                frameSymbolSting = frameSymbolSting + "◼"

    print(30 * "\n")
    print("#" * TERMINALWIDTH)
    formatString("")
    formatString(" Received frames")

    for i in range(math.ceil(len(frameSymbolSting) / 40)):
        formatString(frameSymbolSting[i*40:(i+1)*40])

    formatString("")
    formatString(frame.replace("\n", ""))
    formatString("")
    formatString("totalFrames=" + str(totalPackets))
    formatString("receivedFrames=" + str(len(output)))
    formatString("receivedCorrectFrames=" + str(correctCount))
    formatString("correctPercentage=" + str(int(correctCount/count *100)) + "%")
    formatString("currentCorrect=" + str(correct))
    formatString("duration=" + str(int(time.time() - startTime)) + "s")
    formatString("relativeTransferspeed=" + str(int(correctCount * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))) + "b/s")
    formatString("absoluteTransferspeed=" + str(int(len(output) * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))) + "b/s")
    formatString("")

    print("#" * TERMINALWIDTH)
    print()

    return(tempTotalPackets)



def printReport(frameNumber, frame, count, totalPackets, output, correct, tempTotalPackets, correctCount, startTime):

    print("__________ Run at " + str(startTime) + " __________")
    print("GAPLENGHT: " + str(GAPLENGHT))
    print("PREAMBLELENGHT: " + str(PREAMBLELENGHT))
    print("PAYLOADLENGHT: " + str(PAYLOADLENGHT))
    print("DATARATE: " + str(DATARATE))
    print("frequency: " + str(int(1/DATARATE)) + "b/s")
    print("totalPackets: " + str(totalPackets))
    print("totalBits: " + str(totalPackets * TOTALLENGHT))
    print()

    print("Count: " + str(count))
    print("correctCount: " + str(correctCount))
    print("correctPercentage=" + str(int(correctCount/count *100)) + "%")

    print("Starttime: " + str(startTime))
    print("Endtime: " + str(time.time()))
    print("Duration: " + str(time.time() - startTime))
    print("Missedframes: " + str(int(count - (time.time() - startTime) / TOTALLENGHT)))
    print("correctDataSpeed: " + str(int(correctCount * TOTALLENGHT / (time.time() - startTime))))
    print("correctPayloadSpeed: " + str(int(correctCount * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))))
    print("usefullPayloadSpeed: " + str(int(len(output) * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))))
    print()
    print("relativeTransferspeed=" + str(int(correctCount * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))) + "b/s")
    print("absoluteTransferspeed=" + str(int(len(output) * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))) + "b/s")





def writeReportToFile(frameNumber, frame, count, totalPackets, output, correct, tempTotalPackets, correctCount, startTime):
    ###### Write report ######
    f = open("results.csv", "a")
    f.write("\n")
    f.write(str(GAPLENGHT) + ",    ")
    f.write(str(PREAMBLELENGHT) + ",    ")
    f.write(str(PAYLOADLENGHT) + ",    ")
    f.write(str(DATARATE) + ",    ")
    f.write(str(int(1/DATARATE)) + "b/s" + ",    ")
    f.write(str(totalPackets) + ",    ")
    f.write(str(totalPackets * TOTALLENGHT) + ",    ")


    f.write(str(count) + ",    ")
    f.write(str(correctCount) + ",    ")
    f.write(str(int(correctCount/count *100)) + "%" + ",    ")

    f.write(str(startTime) + ",    ")
    f.write(str(time.time()) + ",    ")
    f.write(str(time.time() - startTime) + ",    ")
    f.write(str(int(count - (time.time() - startTime) / TOTALLENGHT)) + ",    ")
    f.write(str(int(correctCount * TOTALLENGHT / (time.time() - startTime))) + ",    ")
    f.write(str(int(correctCount * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))) + ",    ")
    f.write(str(int(len(output) * (PAYLOADLENGHT - PARITYLENGHT) / (time.time() - startTime))) + ",    ")
    f.write(str(DISTANCE))

    f.close()



