const byte ledPin = 13;
const byte sensorPin = 2;

unsigned long frameTime = 2000;
unsigned long halfFrameTime = frameTime / 2;
unsigned long startWaitTime = frameTime / 8;
unsigned long endWaitTime = frameTime - startWaitTime;
unsigned long framePlusWaitTime = frameTime + startWaitTime;
long frameCorrection = 0;
bool frameSend = false;

unsigned long relativeFrameTime = 0;

unsigned long previousMicros = 0;
unsigned long currentMicros = 0;

void(* resetFunc) (void) = 0;


void setup() {
  pinMode(sensorPin, INPUT_PULLUP);
  Serial.begin(1000000);

}

void loop() {
    Serial.println(pulseIn(sensorPin, 1));

}
