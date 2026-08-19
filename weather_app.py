import requests
from config import weather_api_key
from datetime import datetime, timezone, timedelta


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": weather_api_key,
        "units": "metric"
    }
    response = requests.get(url, params=params, timeout=10)
    return response


def display_weather(data):
    city = data["name"]
    country = data["sys"]["country"]
    timestamp = data["dt"]
    timezone_offset = data["timezone"]
    city_timezone = timezone(timedelta(seconds=timezone_offset))
    local_time = datetime.fromtimestamp(timestamp, tz=city_timezone)
    weather_date = local_time.strftime("%d-%m-%Y")
    weather_time = local_time.strftime("%H:%M")
    print(f"\nWeather in {city}, {country}")
    print(f"Date (DD-MM-YYYY): {weather_date}")
    print(f"Time (HH:MM): {weather_time}")
    print(f"Temperature: {data['main']['temp']:.1f} °C")
    print(f"Feels like: {data['main']['feels_like']:.1f} °C")
    print(f"Weather: {data['weather'][0]['description'].capitalize()}")
    print(f"Humidity: {data['main']['humidity']} %")
    print(f"Wind speed: {data['wind']['speed']} m/s")


def show_weather_for_city(city):
    try:
        response = get_weather(city)
        if response.status_code == 200:
            data = response.json()
            display_weather(data)
        elif response.status_code == 404:
            print("City not found.")
        elif response.status_code == 401:
            print("Invalid API key.")
        else:
            print(f"Error fetching weather data. Status code: {response.status_code}")
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")
    except requests.exceptions.ConnectionError:
        print("No internet connection. Please check your internet connection.")
    except requests.exceptions.RequestException:
        print("An error occurred while fetching weather data. Please try again later.")


def main():
    print("=" * 30)
    print("         WEATHER APP")
    print("=" * 30)
    while True:
        city = input("Enter city: ").strip()
        if not city:
            print("City name cannot be empty.")
            continue
        show_weather_for_city(city)
        while True:
            again = input("\nSearch another city? (y/n): ").strip().lower()
            if again == "y":
                break
            elif again == "n":
                print("Goodbye!")
                return
            else:
                print("Please enter 'y' or 'n'.")
if __name__ == "__main__":
    main()
