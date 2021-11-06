unsigned long bitTime = 10000;
unsigned long halfBitTime = bitTime / 2;
unsigned long previousMillis = 0;
const int ledPin =  LED_BUILTIN;

int receivedBit = 0;
int ledState = 0;

bool received = false;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115201);
}

void loop() {
  if (Serial.available() > 0) {
    receivedBit = Serial.read();
    Serial.println(receivedBit);
    received = true;
  }
  
  unsigned long currentMillis = micros();
  if (currentMillis - previousMillis >= bitTime) {
    received = false;
    previousMillis = currentMillis;
    if(receivedBit == 48){
      ledState = 0;
    } else if(receivedBit == 49){
      ledState = 1;
    }
    digitalWrite(ledPin, ledState);
  }

  if (currentMillis - previousMillis >= halfBitTime && received) {
    digitalWrite(ledPin, ledState * -1 + 1);
  }
}
