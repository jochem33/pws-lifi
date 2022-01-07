
GAPLENGHT = 24
PREAMBLELENGHT = 24
PACKETNUMLENGHT = 16
PARITYLENGHT = 16
PAYLOADLENGHT = 256
TOTALLENGHT = GAPLENGHT + PREAMBLELENGHT + PACKETNUMLENGHT + PAYLOADLENGHT
TIMEOUTTIME = 6
TESTTIME = 10



testValues = [
    {
        "GAPLENGHT": 24,
        "PREAMBLELENGHT": 24,
        "PACKETNUMLENGHT": 16,
        "PARITYLENGHT": 16,
        "PAYLOADLENGHT": 32,
        "TIMEOUTTIME": 6,
        "TESTTIME": 450
    }
]


# testValues = [
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 32,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 64,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 128,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 192,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 320,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 384,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 448,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 512,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 640,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 768,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 896,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 1024,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },



#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 32,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 64,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 128,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 192,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 320,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 384,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 448,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 512,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 640,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 768,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 896,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 1024,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },





#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 32,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 64,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 128,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 192,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 320,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 384,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 448,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 512,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 640,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 768,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 896,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 1024,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },




#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 32,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 64,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 128,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 192,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 320,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 384,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 448,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 512,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 640,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 768,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 896,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 1024,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },




#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 32,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 64,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 128,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 192,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 320,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 384,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 448,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 512,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 640,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 768,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 896,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 1024,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },




#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 32,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 64,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 128,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 192,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 320,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 384,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 448,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 512,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 640,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 768,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 896,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 1024,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },


















#     {
#         "GAPLENGHT": 8,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 16,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 32,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 40,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 48,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 64,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },

#     {
#         "GAPLENGHT": 8,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 16,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 32,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 40,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 48,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 64,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },


#     {
#         "GAPLENGHT": 8,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 16,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 32,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 40,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 48,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 64,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },


#     {
#         "GAPLENGHT": 8,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 16,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 32,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 40,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 48,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 64,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },



#     {
#         "GAPLENGHT": 8,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 16,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 32,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 40,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 48,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 64,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     }
# ]



































# testValues = [
    
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 320,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 352,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 384,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 416,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 448,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 480,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 512,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 544,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 576,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 608,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 640,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 672,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 704,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 736,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 768,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 832,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 896,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 960,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 1024,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 1088,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },




#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 30
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 60
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 90
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 120
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 150
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 450
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 600
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 1200
#     },






#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 30
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 60
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 90
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 120
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 150
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 450
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 600
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 1200
#     },






#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 30
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 60
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 90
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 120
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 150
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 450
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 600
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 1200
#     },





#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 30
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 60
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 90
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 120
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 150
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 450
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 600
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 1200
#     },






#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 30
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 60
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 90
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 120
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 150
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 450
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 600
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 1200
#     },





#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 30
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 60
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 90
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 120
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 150
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 450
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 600
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 1200
#     },





#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 30
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 60
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 90
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 120
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 150
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 450
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 600
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 1200
#     },





#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 30
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 60
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 90
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 120
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 150
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 450
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 600
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 1200
#     },




#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 30
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 60
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 90
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 120
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 150
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 450
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 600
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 1200
#     },




#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 30
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 60
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 90
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 120
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 150
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 180
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 300
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 450
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 600
#     },
#     {
#         "GAPLENGHT": 24,
#         "PREAMBLELENGHT": 24,
#         "PACKETNUMLENGHT": 16,
#         "PARITYLENGHT": 16,
#         "PAYLOADLENGHT": 256,
#         "TIMEOUTTIME": 6,
#         "TESTTIME": 1200
#     }
# ]