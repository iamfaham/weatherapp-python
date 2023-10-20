import requests

API_KEY = "16abde96491a8b119dd8d6e3496a4609"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name for weather data: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    print(f"{city}'s weather today")
    print("Weather: ", weather)
    print("Temperature:", round(temperature - 273.15, 2), "`C")

else:
    print("Unknown error occurred!")
