import requests
import json


url = "https://jsonplaceholder.typicode.com/users"


response = requests.get(url)


if response.status_code == 200:
    print("API call successful ")
else:
    print("API failed ")
    exit()


data = response.json()


print("\nUser List:")
for user in data:
    print("Name :", user["name"])
    print("Email:", user["email"])
    print("-" * 20)


with open("users.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data saved to users.json file ")
