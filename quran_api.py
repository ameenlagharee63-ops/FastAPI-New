from fastapi import FastAPI
import requests

app = FastAPI(title="Quran API")

BASE_URL = "https://ummahapi.com"


@app.get("/")
def home():
    return {
        "message": "Quran API Project is running"
    }


@app.get("/surah/{surah_number}")
def get_surah(surah_number: int):
    url = f"{BASE_URL}/api/quran/surah/{surah_number}"
    response = requests.get(url)
    return response.json()


@app.get("/surahs")
def get_surahs():
    url = f"{BASE_URL}/api/quran/surahs"
    response = requests.get(url)
    return response.json()



@app.get("/surah/{surah_number}/ayahs")
def get_ayahs(surah_number: int):
    url = f"{BASE_URL}/api/quran/surah/{surah_number}"

    response = requests.get(url) 
    return response.json()

   

