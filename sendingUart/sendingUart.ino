
#include <SoftwareSerial.h>
int speedL, speedR;
SoftwareSerial mySerial(4, 5); // RX, TX

void setup()  
{
  
  Serial.begin(115201);
  Serial.flush();
  mySerial.begin(115201);
  mySerial.flush();

  speedL = 123;          // for testing
  speedR = -456;
}

void loop() 
{
  if (Serial.available()) { 
    int bit = mySerial.parseInt(); 

    mySerial.print(speedR);
    mySerial.print('\n');
  }
}
