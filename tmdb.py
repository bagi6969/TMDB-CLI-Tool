import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://api.themoviedb.org/3"

def fetch_movie(list_type: str, api_key:str):
    endpoints = {
        "playing": "movie/now_playing",
        "popular": "movie/popular",
        "top": "movie/top_rated",
        "upcoming": "movie/upcoming",
    }

    if list_type not in endpoints:
        raise ValueError("Invalid type. Must be one of: playing, popular, top, upcoming")

    url = f"{BASE_URL}/{endpoints[list_type]}"
    params = {
        "api_key": api_key,
        "language": "en-US"
    }

    response = requests.get(url, params=params)

    if response.status_code == 401:
        raise ValueError(f"Invalid API KEY {url},{API_KEY}")
    elif response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}")

    return response.json().get("results", [])
