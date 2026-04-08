import pandas as pd
import random

num_rows = 1500

data = []

locations = [
    "Whitefield",
    "Electronic City",
    "MG Road",
    "BTM Layout",
    "Yelahanka",
    "Indiranagar",
    "Marathahalli",
    "Hebbal",
    "KR Puram",
    "Jayanagar"
]

patrol_units = [
    "Patrol Unit A",
    "Patrol Unit B",
    "Patrol Unit C",
    "Patrol Unit D",
    "Patrol Unit E"
]


for i in range(num_rows):
    
    rain = random.randint(0, 4095)
    traffic = random.randint(0, 1)
    distance = random.randint(5, 200)
    temperature = random.randint(20, 40)
    humidity = random.randint(40, 100)
    visibility = random.randint(10, 100)
    speed = random.randint(20, 100)

    location = random.choice(locations)
    patrol = random.choice(patrol_units)

    # Generate random Indian phone number
    phone = "9" + "".join([str(random.randint(0,9)) for _ in range(9)])

    if rain > 3000 and distance < 20 and traffic == 1:
        risk = "Critical"
        
    elif rain > 2000 or distance < 40 or visibility < 30:
        risk = "High"
        
    elif rain > 1000 or speed > 80:
        risk = "Caution"
        
    else:
        risk = "Safe"

    data.append([
        rain, traffic, distance, temperature,
        humidity, visibility, speed,
        location, patrol, phone, risk
    ])


df = pd.DataFrame(data, columns=[
    "Rain",
    "Traffic",
    "Distance",
    "Temperature",
    "Humidity",
    "Visibility",
    "Speed",
    "Location",
    "Patrol_Unit",
    "Phone_Number",
    "Risk"
])

df['Rain_mm'] = (df['Rain'] / 4095) * 50
df['Rain_cm'] = df['Rain_mm'] / 10

df.to_excel("rain_traffic_dataset.xlsx", index=False)
df.to_csv("rain_traffic_dataset.csv", index=False)

print(" Dataset successfully created!")
print("Total rows:", len(df))
print("\nSample data:")
print(df.head())
