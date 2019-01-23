#define OFFMODE -1
#define ONMODE 0
#define BLINKMODE 1
const int pinLED = 13;

float flt; float sum=0;
int flag = 0;

void setup() {
  pinMode(pinLED,OUTPUT);
  Serial.begin(115200);
}

void loop() {
  if(Serial.available()){
    sum = Serial.parseFloat();
    flag =1;
    Serial.println(flag);
    Serial.println(sum);
  }
  else{
    flag = 0;
    Serial.println(flag);
    Serial.println(2.5);      
    Serial.println(12.3);
    delay(100);
  }



}
