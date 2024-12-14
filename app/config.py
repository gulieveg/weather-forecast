from decouple import config


class Config:
    SECRET_KEY = config("SECRET_KEY")
    WEATHER_API_KEY = config("WEATHER_API_KEY")
    WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
    WEATHER_UNITS = "metric"
    WEATHER_LANG = "en"
