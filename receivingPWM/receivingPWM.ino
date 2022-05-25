const byte ledPin = 13;
const byte sensorPin = 2;


const unsigned long symbolLenght = 1000;
const unsigned long endSymbolGap = 400;
const int symbolCount = 16;
const unsigned long fragmentLenght = (symbolLenght - endSymbolGap) / symbolCount;


unsigned long startBitTime = 0;
unsigned long messuredBitTime = 0;

int receivedSymbol = 0;
int compareSymbol = 1;

void setup() {
  Serial.begin(250000);

  pinMode(sensorPin, INPUT_PULLUP);

}

void loop() {
  messuredBitTime = pulseIn(sensorPin, 1);
  receivedSymbol = messuredBitTime / fragmentLenght;
  Serial.println(receivedSymbol - 1);

}