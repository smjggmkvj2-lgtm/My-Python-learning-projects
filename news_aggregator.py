import requests
from config import news_api_key
topic = input("Enter the topic you want to search news for: ")
url = "https://newsapi.org/v2/everything?q=" + topic + "&apiKey=" + news_api_key
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Here are articles about", topic)
    for article in data["articles"][:5]:
        print("\nTitle:", article["title"])
        print("Source:", article["source"]["name"])
        print("Description:", article["description"])
        print("Published At:", article["publishedAt"])
        print("URL:", article["url"])
else:
    print("Error fetching news data")