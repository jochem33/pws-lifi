const byte ledPin = 13;
const byte sensorPin = 2;

const word frameTime = 1000000;
const word waitTime = frameTime / 4;
const word framePlusWaitTime = frameTime + waitTime;
unsigned long previousMicros = 0;

byte previousState = 0;
bool sendBit = false;

void setup() {
  Serial.begin(115201);

  pinMode(sensorPin, INPUT_PULLUP);
  previousState = digitalRead(sensorPin);
}

void loop() {
  if(sendBit == false){
    byte state = digitalRead(sensorPin);
    if(state != previousState){
      Serial.println(previousState);
      sendBit = true;
    }
    previousState = state;  
    
  }

  unsigned long currentMicros = micros();

  if (currentMicros - previousMicros >= frameTime) {
    previousMicros = currentMicros;
    sendBit = false;
  }
}
