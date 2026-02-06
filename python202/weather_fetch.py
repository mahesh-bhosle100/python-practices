import requests

class Weather:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("City not found")
            return

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        print(f"City: {city}")
        print(f"Temperature: {temp} °C")
        print(f"Weather: {condition}")


def main():
    api_key = "60a8bf52f2168e90c3d6fe9761b07612"   # paste your API key
    city = input("Enter city name: ")

    weather = Weather(api_key)
    weather.get_weather(city)


main()
