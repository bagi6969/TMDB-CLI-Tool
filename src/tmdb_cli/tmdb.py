import requests

def fetch_movie(list_type: str, api_key: str):
    endpoints = {
        "playing": "movie/now_playing",
        "popular": "movie/popular",
        "top": "movie/top_rated",
        "upcoming": "movie/upcoming"
    }

    if list_type not in endpoints:
        raise ValueError("Invalid type. Must be one of: playing, popular, top, upcoming")

    url = f"https://api.themoviedb.org/3/{endpoints[list_type]}"
    params = {"api_key": api_key, "language": "en-US"}
    res = requests.get(url, params=params)

    if res.status_code == 401:
        raise ValueError("❌ Invalid API key")
    elif res.status_code != 200:
        raise ValueError(f"Request failed: {res.status_code}")

    return res.json().get("results", [])
