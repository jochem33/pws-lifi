const byte ledPin = 13;
const byte sensorPin = 2;
volatile byte state = LOW;

void setup() {
//  pinMode(ledPin, OUTPUT);
  pinMode(sensorPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(sensorPin), sendSerial, CHANGE);

}

void loop() {
//  digitalWrite(ledPin, state);
}

void sendSerial() {
   Serial.println(digitalRead(sensorPin));
}
