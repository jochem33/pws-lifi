int sensorPin = A0;
int ledPin = 6;
int sensorValue = 0;
int digitalSensorValue = 0;

int minimum = 2400;
int maximum = 0;
int average = 500;

int ledStatus = LOW;

const long dataRate = 10000;



unsigned long previousMicros = 0;


void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115201);
}


void loop() {  
  unsigned long currentMicros = micros();

  if (currentMicros - previousMicros >= dataRate) {
    previousMicros = currentMicros;
    
    sensorValue = analogRead(sensorPin);
    digitalSensorValue = digitalRead(sensorPin);
    
    Serial.println(sensorValue);
    Serial.print(",");
    Serial.println(digitalSensorValue * 200);
  }

}
