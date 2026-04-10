#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>


#define WIFI_SSID "Wokwi-GUEST"
#define WIFI_PASS ""


#define API_KEY "MY307PGVNJ7D0UF8"
#define SERVER "http://api.thingspeak.com/update"


#define RAIN_PIN 34        
#define TRAFFIC_PIN 14     
#define TRIG 16             
#define ECHO 18
#define DHTPIN 4           
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

int rainValue = 0;
int traffic = 0;
long distance = 0;
float temperature = 0;

String rainStatus, trafficStatus, distanceStatus, risk;

unsigned long lastUploadTime = 0;

void setup() {
  Serial.begin(115200);

  pinMode(TRAFFIC_PIN, INPUT_PULLDOWN);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  dht.begin();

  Serial.println("Connecting to WiFi...");
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected!");
}

long getDistance() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  long duration = pulseIn(ECHO, HIGH);
  return duration * 0.034 / 2;
}

void loop() {

  rainValue = analogRead(RAIN_PIN);
  traffic = digitalRead(TRAFFIC_PIN);
  distance = getDistance();
  temperature = dht.readTemperature();

  if (rainValue < 1000) {
    rainStatus = "LOW";
  } else if (rainValue < 2500) {
    rainStatus = "MEDIUM";
  } else {
    rainStatus = "HIGH";
  }

  if (traffic == 1) {
    trafficStatus = "TRAFFIC PRESENT";
  } else {
    trafficStatus = "NO TRAFFIC";
  }

  if (distance > 50) {
    distanceStatus = "SAFE";
  } else if (distance > 20) {
    distanceStatus = "MEDIUM";
  } else {
    distanceStatus = "DANGEROUS";
  }

  if (rainStatus == "HIGH" && distanceStatus == "DANGEROUS" && traffic == 1) {
    risk = "CRITICAL";
  }
  else if (rainStatus == "MEDIUM" || distanceStatus == "MEDIUM") {
    risk = "HIGH";
  }
  else if (rainStatus == "LOW") {
    risk = "CAUTION";
  }
  else {
    risk = "SAFE";
  }

  
  Serial.println("------ DATA ------");
  Serial.println("Rain: " + String(rainValue) + " (" + rainStatus + ")");
  Serial.println("Traffic: " + trafficStatus);
  Serial.println("Distance: " + String(distance) + " cm (" + distanceStatus + ")");
  Serial.println("Temperature: " + String(temperature));
  Serial.println("Risk Level: " + risk);
  Serial.println("------------------");

 
  if (millis() - lastUploadTime >= 20000) {

    if (WiFi.status() == WL_CONNECTED) {

      HTTPClient http;

      String url = String(SERVER) + "?api_key=" + API_KEY +
                   "&field1=" + String(rainValue) +
                   "&field2=" + String(traffic) +
                   "&field3=" + String(distance) +
                   "&field4=" + String(temperature);

      http.begin(url);
      int httpResponseCode = http.GET();

      if (httpResponseCode > 0) {
        Serial.println("Uploaded to ThingSpeak ");
      } else {
        Serial.println("Upload failed ");
      }

      http.end();
    }

    lastUploadTime = millis();
  }

  delay(1000);
}
