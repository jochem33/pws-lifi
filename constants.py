DATARATE = 0.002

BAUDRATE = 1000000

DISTANCE = 95

GAPLENGHT = 24
PREAMBLELENGHT = 128
PACKETNUMLENGHT = 16
PARITYLENGHT = 16
PAYLOADLENGHT = 256
# ENDOFFRAMELENGHT = 8
TOTALLENGHT = GAPLENGHT + PREAMBLELENGHT + PACKETNUMLENGHT + PAYLOADLENGHT

SYMBOLCOUNT = 32

TIMEOUTTIME = 10

TESTTIME = 180

FRAMESTART = ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '1']
ANTIFRAMESTART = ["0","1","0","1","0","1","0","1", "0", "1","0","1","0","1","0","0"]

RECEIVINGDEVICE = '/dev/cu.usbmodem14201'
SENDINGDEVICE = '/dev/cu.usbserial-14110'

INPUTFILE = 'input.html'
OUTPUTFILE = 'output.html'
