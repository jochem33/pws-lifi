const byte ledPin = 13;
const byte sensorPin = 2;

unsigned long frameTime = 10000;
unsigned long startWaitTime = frameTime / 4;
unsigned long endWaitTime = frameTime - startWaitTime;
unsigned long framePlusWaitTime = frameTime + startWaitTime;
unsigned long frameCorrection = 0;
bool frameSend = false;

unsigned long relativeFrameTime = 0;

unsigned long previousMicros = 0;
unsigned long currentMicros = 0;


void setup() {
//  pinMode(ledPin, OUTPUT);
  Serial.begin(115201);

  pinMode(sensorPin, INPUT_PULLUP);

  synchronize();
  attachInterrupt(digitalPinToInterrupt(sensorPin), sendSerial, CHANGE);
  currentMicros = micros();
}

void loop() {
  currentMicros = micros();
  relativeFrameTime = currentMicros - previousMicros;

  if (relativeFrameTime >= frameTime) {
    previousMicros = currentMicros;
    relativeFrameTime = 0;
    frameSend = false;
  }

//  if(relativeFrameTime > startWaitTime && relativeFrameTime < endWaitTime && frameSend == false){
//    Serial.println(digitalRead(sensorPin) * 100000);
//    Serial.print(",");
//    Serial.println(relativeFrameTime);
//    frameSend = true;
//  }
}

void sendSerial() {
  if(relativeFrameTime > startWaitTime && relativeFrameTime < endWaitTime && frameSend == false){
    Serial.println(digitalRead(sensorPin));
    Serial.print(",");
    Serial.println(float(frameTime) / relativeFrameTime);
    frameSend = true;
  }
}

void synchronize() {
  bool unSynced = true;
  byte previousState = digitalRead(sensorPin);
  previousMicros = micros();
  while(unSynced){
    byte state = digitalRead(sensorPin);
    if(state != previousState){
      unSynced = false;
      frameCorrection = micros() - previousMicros;
    }  
  }
}