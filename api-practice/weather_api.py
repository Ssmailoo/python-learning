import requests
import json

API_KEY = "db22b4e1eb9276d53f1f5457cf69fa53"
city = "Makassar"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

print(response.status_code)
print(response.json())

data = response.json()

print("Kota:", data['name'])
print("Suhu:", data['main']['temp'], "°C")
print("Kondisi:", data['weather'][0]['description'])
print("kelembaban:", data['main']['humidity'], "%")


data_1 = {
    "humidity": data['main']['humidity'],
    "weather": data['weather'][0]['description'],
    "clouds": data['clouds']['all'],
    "datetime": data['dt'],
    "timezone": data['timezone']
}
try:
    with open("history.json",mode='r') as file:
        history = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    history = []
    
history.append(data_1)

with open("history.json",mode='w') as file:
    json.dump(history, file, indent=2)

    

