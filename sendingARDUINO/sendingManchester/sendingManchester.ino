unsigned long bitTime = 100000;
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
    Serial.println(receivedBit);
//    Serial.print(",");
    received = true;
    ledState = receivedBit - 48;
    
    digitalWrite(ledPin, ledState);
    previousMicros = micros();
  }

  if(previousMicros - micros() < halfBitTime){
     Serial.println(halfBitTime);
     digitalWrite(ledPin, ledState * -1 + 1);
  }
}







//
//
//unsigned long bitTime = 100000;
//unsigned long halfBitTime = bitTime / 2;
//unsigned long previousMillis = 0;
//const int ledPin =  LED_BUILTIN;
//
//int receivedBit = 0;
//int ledState = 0;
//
//bool received = false;
//
//void setup() {
//  pinMode(ledPin, OUTPUT);
//  Serial.begin(115201);
//}
//
//void loop() {
//  if (Serial.available() > 0) {
//    receivedBit = Serial.read();
//    Serial.println(receivedBit);
//    received = true;
//  }
//  
//  unsigned long currentMillis = micros();
//  if (currentMillis - previousMillis >= bitTime) {
//    received = false;
//    previousMillis = currentMillis;
//    ledState = receivedBit - 48;
//    digitalWrite(ledPin, ledState);
//  }
//
//  if (currentMillis - previousMillis >= halfBitTime && received) {
//    if(ledState == 1){
//       digitalWrite(ledPin, 0);
//     } else {
//       digitalWrite(ledPin, 1);
//     }
//  }
//}
