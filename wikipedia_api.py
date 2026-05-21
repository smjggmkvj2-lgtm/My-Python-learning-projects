import requests

ask = input("Enter topic: ")

url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + ask

headers = {"User-Agent":  "MyWikipediaApp/1.0"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("\nTitle:" , data["title"])
    print("\nSummary:", data["extract"])
else:
    print("Article was not found")