# Weather Forecast

This is simple weather forecast application built using Flask, which fetches weather data from an external API and displays it to the user. The application supports searching for weather in different cities and shows temperature, weather description, and more.

## Features

- **Weather Forecast**: Fetches and displays the current weather for given city.
- **Language Support**: The app currently supports English language for weather data.
- **Responsive Design**: The interface is designed to work on desktop.

## Requirements

- Python 3.x
- Flask
- Requests
- .env file to store environment variables

## Installation

1. Clone the repository:

```bash
    git clone https://github.com/gulieveg/weather-forecast.git
```

2. Navigate to the project directory:

```bash
    cd weather-forecast
```

3. Install the required dependencies:

```bash
    python -m pip install flask requests
```

4. Set up your .env file to store sensitive information like the weather API key:

```bash
    WEATHER_API_KEY=<WEATHER_API_KEY>
    WEATHER_UNITS=<WEATHER_UNITS>
    WEATHER_LANG=<WEATHER_LANG>
```

5. Run the application:

```bash
    python run.py
```

6. The app will be available at `http://127.0.0.1:5000/` by default. You can change the host and port by modifying the .env file.
