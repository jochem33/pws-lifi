import math

totalPackets = 32
output = {1: "a", 5: "b", 6: "b", 7: "b", 10: "b", 11: "a", 15: "b", 16: "b", 13: "b", 20: "b", 40:""}

terminalWidth = 70


def formatString(text):
    print("# " + text + " "* (terminalWidth - len(text) - 4) + " #")


frameSymbolSting = ""
if(totalPackets < 35000):
    for i in range(totalPackets):
        if(i + 1 not in output):
            frameSymbolSting = frameSymbolSting + "◻ "
        else:
            frameSymbolSting = frameSymbolSting + "◼ "

print(30 * "\n")
print("#" * terminalWidth)
formatString("")
formatString(" Received frames")

for i in range(math.ceil(len(frameSymbolSting) / 40)):
    formatString(frameSymbolSting[i*40:(i+1)*40])

formatString("")
formatString("totalFrames=" + str(totalPackets))
formatString("receivedFrames=" + str(len(output)))
formatString("receivedCorrectFrames=" + str(correctCount))
formatString("correctPercentage=" + str(int(correctCount/count *100)) + "%")
formatString("currentCorrect=" + str(correct))
formatString("duration=" + str(int(time.time() - startTime)) + "s")
formatString("")

print("#" * terminalWidth)


print()
input()