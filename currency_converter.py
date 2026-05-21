import requests
amount = float(input("Enter the amount to convert: "))
first_currency = input("Enter the source currency (e.g., 'USD'): ")
second_currency = input("Enter the target currency (e.g., 'EUR'): ")
url = "https://api.exchangerate-api.com/v4/latest/" + first_currency
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    if second_currency in data["rates"]:
        rate = data["rates"][second_currency]
        converted_amount = amount * rate
        print(f"{amount} {first_currency} is {converted_amount} in {second_currency}")
    else:
        print("Currency not found.")
else:
    print("Error fetching exchange rates.")      