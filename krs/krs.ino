#include <dht.h>

#define outPinDHT 22  
dht DHT;  

const int buttonPin1 = 49;
const int buttonPin2 = 48;
float oldTemp = 0;
float oldHum = 0;
int val1;
int val2;
int on;

ISR(INT0_vect){
  on = 0;
}

void setup() {
  Serial.begin(9600);
  
  noInterrupts();
  EIMSK |= (1<<INT0);
  EICRA &= ~(1<<ISC00);
  EICRA |= (1 <<ISC01);
  interrupts();

  DDRC = 0x0F;

  pinMode(buttonPin1, INPUT_PULLUP);
  digitalWrite(buttonPin1, HIGH); 
  
  pinMode(buttonPin2, INPUT_PULLUP);
  digitalWrite(buttonPin2, HIGH); 

}

void loop() {
  int readData = DHT.read11(outPinDHT);
  float t = DHT.temperature;  
  float h = DHT.humidity; 
  
  if (t != oldTemp || h != oldHum) { 
    Serial.print(t);
    Serial.print(h);
  
    Serial.println("");
    oldTemp = t;
    oldHum = h;
  }
  
  val1 = digitalRead(buttonPin1);
  val2 = digitalRead(buttonPin2);

  int byte = Serial.read();
  if (byte == 11) {
    val1 = LOW;
  }
  
  if (val1 == LOW) {
    on = 1;
  }
  
  while (on == 1) {
      int byte = Serial.read();
      if (byte == 12) {
        val1 = HIGH;
      }
      if (val1 == HIGH) {
         on =0;
      }
      PORTC = 0b00000001;
      delay(200);
      PORTC = 0b00000100;
      delay(200);
      PORTC = 0b00001000;
      delay(200); 
      PORTC = 0b00000010;
      delay(200);
  }
}
