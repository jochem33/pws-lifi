const byte ledPin = 13;
const byte sensorPin = 2;

unsigned long frameTime = 1500;
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

  if (Serial.available() > 0) {
     resetFunc();
  }
}

void sendSerial() {
  if(relativeFrameTime > startWaitTime && relativeFrameTime < endWaitTime && frameSend == false){
    frameCorrection+= halfFrameTime - relativeFrameTime;
//    Serial.print(digitalRead(sensorPin) * 100 + endWaitTime);
//    Serial.print(",");
//    Serial.print(relativeFrameTime);
//    Serial.print(",");
//    Serial.println(endWaitTime);
    Serial.println(digitalRead(sensorPin));
    frameSend = true;
  }
}
