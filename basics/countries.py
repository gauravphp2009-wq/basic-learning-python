import requests

response = requests.get("https://api.first.org/data/v1/countries")
data = response.json()

for code, info in data["data"].items():
    if info["region"] == "Central America":
        print(code, "-", info["country"])