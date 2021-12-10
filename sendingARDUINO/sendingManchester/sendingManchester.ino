unsigned long bitTime = 2000;
unsigned long halfBitTime = bitTime / 2;
unsigned long previousMicros = 0;
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
    Serial.println(ledState);
    received = true;
    ledState = receivedBit - 48;
    
    digitalWrite(ledPin, ledState);
    previousMicros = micros();
  }

  if(micros() - previousMicros > halfBitTime){
    Serial.println(ledState);
    digitalWrite(ledPin, ledState * -1 + 1);
  }
}
