import requests
from config import api_key
url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("\nTitle:" , data["title"])
    print("\ndate:", data["date"])
    print("\nExplanation:", data["explanation"])
    print("\nURL:", data["url"])
else:
    print("Error fetching data from NASA API")

with open("nasa_photo.jpg", "wb") as f:
    f.write(requests.get(data["url"]).content)
print("Photo saved as nasa_photo.jpg")