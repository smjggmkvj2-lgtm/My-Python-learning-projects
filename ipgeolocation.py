import requests
ip = input("Enter IP address: ")

url = "https://ipapi.co/" + ip + "/json/"
response = requests.get(url)
if response.status_code == 200: 
    data = response.json()
    print("\nIP:", data["ip"])
    print("\nCity:", data["city"])
    print("\nRegion:", data["region"])
    print("\nCountry:", data["country_name"])
    print("\nLatitude:", data["latitude"])
    print("\nLongitude:", data["longitude"])
    print("\nTimezone:", data["timezone"])
    print("\npostal:", data["postal"])
else:
    print("Error fetching data from IP Geolocation API")