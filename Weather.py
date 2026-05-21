import requests
from config import weather_api_key
city = input("Enter city name: ")
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + weather_api_key + "&units=metric"
response = requests.get(url) 
if response.status_code == 200:
    data = response.json()
    print("\nCity:", data["name"])
    print("\nTemperature:", data["main"]["temp"], "°C")
    print("\nWeather:", data["weather"][0]["description"])
    print("\nHumidity:", data["main"]["humidity"], "%")
    print("\nfeels like:", data["main"]["feels_like"], "°C")
    print("\ntemperature min:", data["main"]["temp_min"], "°C")
    print("\ntemperature max:", data["main"]["temp_max"], "°C")
else:
    print("Error fetching weather data")