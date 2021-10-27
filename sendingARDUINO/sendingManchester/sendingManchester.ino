unsigned long bitTime = 100000;
unsigned long halfBitTime = bitTime / 2;
unsigned long previousMillis = 0;
const int ledPin =  LED_BUILTIN;

char receivedBit = -1;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115201);
}

void loop() {
  if (Serial.available() > 0) {
    receivedBit = Serial.read();
    Serial.println(receivedBit);
  }
  
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= bitTime) {
    previousMillis = currentMillis;
    if(receivedBit >= 0){
      digitalWrite(ledPin, receivedBit);
    } else {
      digitalWrite(ledPin, 1);
    }
    receivedBit = -1;
  }

  if (currentMillis - previousMillis >= halfBitTime) {
    digitalWrite(ledPin, receivedBit * -1 + 1);
  }
}
