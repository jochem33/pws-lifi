
#include <SoftwareSerial.h>
int setL, setR;

SoftwareSerial mySerial(4, 5); // RX, TX

void setup()  
{
  
  Serial.begin(115201);
  Serial.flush();
  mySerial.begin(115201);
  mySerial.flush();
  
}

void loop() 
{
  if (mySerial.available()) {   //read the two speeds

    int setR = mySerial.parseInt(); 
    
    if (mySerial.read() == '\n') {
      Serial.print(", setR = ");
      Serial.println(setR);
    }  
 }
}
