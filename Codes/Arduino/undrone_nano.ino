//Coded by XQuest
//Aditya Parmar
#include <ArduinoMqttClient.h>
#if defined(ARDUINO_SAMD_MKRWIFI1010) || defined(ARDUINO_SAMD_NANO_33_IOT) || defined(ARDUINO_AVR_UNO_WIFI_REV2)
#include <WiFiNINA.h>
#elif defined(ARDUINO_SAMD_MKR1000)
#include <WiFi101.h>
#elif defined(ARDUINO_ARCH_ESP8266)
#include <ESP8266WiFi.h>
#elif defined(ARDUINO_ARCH_ESP32)
#include <WiFi.h>
#endif

#define PIN1 2  //upward
#define PIN2 3  //downward
#define PIN4 4  //left
#define PIN3 5  //right

///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = "";    // your network SSID (name)
char pass[] = "";    // your network password (use for WPA, or use as key for WEP)

// To connect with SSL/TLS:
// 1) Change WiFiClient to WiFiSSLClient.
// 2) Change port value from 1883 to 8883.
// 3) Change broker value to a server with a known SSL/TLS root certificate
//    flashed in the WiFi module.

#define ULTRASONIC_TRIG_PIN 4 // pin trig is D11
#define ULTRASONIC_ECHO_PIN 5


long duration; // variable for the duration of sound wave travel
int distance;
//Coded by XQuest
//Aditya Parmar
WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

const char broker[] = "broker.hivemq.com";
int        port     = 1883;
const char topic[]  = "xquest/test";

const long interval = 1000;
unsigned long previousMillis = 0;

int count = 0;

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);

  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // attempt to connect to WiFi network:
  Serial.print("Attempting to connect to WPA SSID: ");
  Serial.println(ssid);
  while (WiFi.begin(ssid, pass) != WL_CONNECTED) {
    // failed, retry
    Serial.print(".");
    delay(5000);
  }

  Serial.println("You're connected to the network");
  Serial.println();

  // You can provide a unique client ID, if not set the library uses Arduino-millis()
  // Each client must have a unique client ID
  // mqttClient.setId("clientId");

  // You can provide a username and password for authentication
  // mqttClient.setUsernamePassword("username", "password");

  Serial.print("Attempting to connect to the MQTT broker: ");
  Serial.println(broker);

  if (!mqttClient.connect(broker, port)) {
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());

    while (1);
  }

  Serial.println("You're connected to the MQTT broker!");
  Serial.println();
}

void loop() {
  // call poll() regularly to allow the library to send MQTT keep alives which
  // avoids being disconnected by the broker
  mqttClient.poll();
  bool var1 = digitalRead(PIN1);
  bool var2 = digitalRead(PIN2);
  bool var3 = digitalRead(PIN3);
  bool var4 = digitalRead(PIN4);
  if (!var1 && !var2) {
    mqttClient.beginMessage(topic);
    mqttClient.print("reset1");
    mqttClient.endMessage();
  }
  else if (!var3 && !var4) {
    mqttClient.beginMessage(topic);
    mqttClient.print("Forward");
    mqttClient.endMessage();
    }
  else if ((!var1 && !var3) || (!var2 && !var4)) {
    mqttClient.beginMessage(topic);
    mqttClient.print("reset1");
    mqttClient.endMessage();
    mqttClient.beginMessage(topic);
    mqttClient.print("reset2");
    mqttClient.endMessage();
  }
  else if (!var1) {
    mqttClient.beginMessage(topic);
    mqttClient.print("Up");
    mqttClient.endMessage();
    }
  else if (!var2) {
    mqttClient.beginMessage(topic);
    mqttClient.print("Down");
    mqttClient.endMessage();
    }
  else if (!var3) {
    mqttClient.beginMessage(topic);
    mqttClient.print("Left");
    mqttClient.endMessage();}
  else if (!var4) {
    mqttClient.beginMessage(topic);
    mqttClient.print("Right");
    mqttClient.endMessage();
    }


  // send message, the Print interface can be used to set the message contents
delay(200);
  Serial.println();
}
//Coded by XQuest
//Aditya Parmar
