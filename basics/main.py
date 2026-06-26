from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/contry")
def home():
    response = requests.get("https://api.first.org/data/v1/countries")
    data = response.json()

    return data["data"]["IN"]