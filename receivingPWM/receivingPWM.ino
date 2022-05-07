const byte ledPin = 13;
const byte sensorPin = 2;


const unsigned long symbolLenght = 1500;
const unsigned long endSymbolGap = 400;
const int symbolCount = 32;
const unsigned long fragmentLenght = (symbolLenght - endSymbolGap) / symbolCount;


unsigned long startBitTime = 0;
unsigned long messuredBitTime = 0;

int receivedSymbol = 0;
int compareSymbol = 1;

void(* resetFunc) (void) = 0;

void setup() {
  Serial.begin(1000000);

  pinMode(sensorPin, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(sensorPin), startStopTimer, CHANGE);
}

void loop() {

}

void startStopTimer() {
  if(digitalRead(sensorPin)){
    startBitTime = micros();
  } else {
    messuredBitTime = micros() - startBitTime;
    receivedSymbol = messuredBitTime / fragmentLenght;
    Serial.println(receivedSymbol - 1);
  } 
}



//
//// with debugging:
//void startStopTimer() {
//  if(digitalRead(sensorPin)){
//    startBitTime = micros();
//  } else {
//    messuredBitTime = micros() - startBitTime;
//    receivedSymbol = messuredBitTime / fragmentLenght;
//    if(receivedSymbol == 1){
//      compareSymbol = 1;
//    }
////    Serial.print(messuredBitTime);
////    Serial.print(",");
//    Serial.print(receivedSymbol - 1);
////    Serial.print(",");
////    Serial.print(fragmentLenght);
//    Serial.print(",");
////    Serial.print(fragmentLenght * 7);
////    Serial.print(",");
//    if(receivedSymbol == compareSymbol){
//      Serial.println(-2);
//    } else {
//      Serial.println(0);
//    }
//    compareSymbol+=1;
////  
//  } 
//}
