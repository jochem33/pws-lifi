const byte ledPin = 13;
const byte sensorPin = 2;

unsigned long frameTime = 100;
unsigned long halfFrameTime = frameTime / 2;
unsigned long startWaitTime = frameTime / 4;
unsigned long endWaitTime = frameTime - startWaitTime;
unsigned long framePlusWaitTime = frameTime + startWaitTime;
long frameCorrection = 0;
bool frameSend = false;

unsigned long relativeFrameTime = 0;

unsigned long previousMicros = 0;
unsigned long currentMicros = 0;


void setup() {
  Serial.begin(115201);

  pinMode(sensorPin, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(sensorPin), sendSerial, CHANGE);
  currentMicros = micros();
}

void loop() {
  currentMicros = micros() + frameCorrection;
  relativeFrameTime = currentMicros - previousMicros;

  if (relativeFrameTime >= frameTime) {
    previousMicros = currentMicros;
    relativeFrameTime = 0;
    frameSend = false;
  }
}

void sendSerial() {
  if(relativeFrameTime > startWaitTime && relativeFrameTime < endWaitTime && frameSend == false){
    frameCorrection+= halfFrameTime - relativeFrameTime;
//    Serial.println(digitalRead(sensorPin) * endWaitTime + startWaitTime);
//    Serial.print(",");
//    Serial.println(relativeFrameTime);
    Serial.println(digitalRead(sensorPin));
    frameSend = true;
  }
}
