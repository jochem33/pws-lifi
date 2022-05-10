
const unsigned long symbolLenght = 1000;
const unsigned long endSymbolGap = 400;
const int symbolCount = 16;
const long capCorrection = 0;
const unsigned long fragmentLenght = (symbolLenght - endSymbolGap) / symbolCount - capCorrection;

unsigned long ontime;

unsigned long previousMicros = 0;
const int ledPin =  LED_BUILTIN;

int receivedSymbol = 0;
int ledState = 0;


void setup() {
  DDRD = B00100000;
//  pinMode(ledPin, OUTPUT);
  Serial.begin(250000);
}

void loop() {
  if (Serial.available() > 0) {
    receivedSymbol = Serial.read() + 1;
//    Serial.println(receivedSymbol);
    ontime = receivedSymbol * fragmentLenght;

    PORTD = B00100000;
//    digitalWrite(ledPin, HIGH);
    previousMicros = micros();
  }

  if(micros() - previousMicros > ontime){
//    digitalWrite(ledPin, LOW);
    PORTD = B00000000;

  }
}
