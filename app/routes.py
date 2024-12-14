from flask import Flask, render_template, request

from app.weather import get_weather

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            weather_data = get_weather(city)
            if not weather_data:
                error_message = "Failed to retrieve weather data"

    return render_template(
        "index.html", weather_data=weather_data, error_message=error_message
    )
