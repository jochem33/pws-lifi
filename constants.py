DATARATE = 0.005

BAUDRATE = 115201

GAPLENGHT = 24
PREAMBLELENGHT = 24
PACKETNUMLENGHT = 16
PAYLOADLENGHT = 256
ENDOFFRAMELENGHT = 8

FRAMESTART = ["0","0","0","0","0","0","0","0", "0","0","0","0","0","0","0","1"]
ANTIFRAMESTART = ["1","1","1","1","1","1","1","1", "1","1","1","1","1","1","1","0"]

RECEIVINGDEVICE = '/dev/cu.usbmodem141201'
SENDINGDEVICE = '/dev/cu.usbserial-14110'

INPUTFILE = 'input.html'
OUTPUTFILE = 'output.html'
