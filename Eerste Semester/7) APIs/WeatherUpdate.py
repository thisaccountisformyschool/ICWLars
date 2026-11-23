import requests
import json

APIkey ="0edfff72378bd669bfaaea227707de42"
lat = 30.061081405056846
lon = 31.21353961821742
data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={APIkey}")

data = data.json()
print(data)