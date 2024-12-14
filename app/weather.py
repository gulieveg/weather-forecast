import requests

from .config import Config


def get_weather(city):
    params = {
        "q": city,
        "appid": Config.WEATHER_API_KEY,
        "units": Config.WEATHER_UNITS,
        "lang": Config.WEATHER_LANG,
    }
    try:
        response = requests.get(Config.WEATHER_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as exception:
        print(f"Request error: {exception}")
        return None
