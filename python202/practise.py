import requests

city = "Mumbai"
apikey = "60a8bf52f2168e90c3d6fe9761b07612"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

response = requests.get(url)
print(response.status_code)

response = requests.get(url)

if response.status_code != 200:
    print("City not found ❌")
    exit()

data = response.json()

temp = data["main"]["temp"] - 273.15
humidity = data["main"]["humidity"]
condition = data["weather"][0]["description"]

print("\n🌦️ Weather Report")
print("------------------")
print("City       :", city)
print("Temperature:", round(temp, 2), "°C")
print("Humidity   :", humidity, "%")
print("Condition  :", condition)