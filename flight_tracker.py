import requests
from config import flight_api_key
flight_num =  input("Enter the flight number you want to track: ")
url = "http://api.aviationstack.com/v1/flights?access_key=" + flight_api_key + "&flight_iata=" + flight_num
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    flight = data["data"][0]
    print("\nFlight:", flight["flight"]["iata"])
    print("\ndeparture:", flight["departure"]["airport"])
    print("\narrival:", flight["arrival"]["airport"])
    print("\nstatus:", flight["flight_status"])
    print("\ndelay:", flight["departure"]["delay"])
    print("\nairline:", flight["airline"]["name"])
    print("\naircraft:", flight["aircraft"]["registration"])
else:
    print("Error fetching flight data")