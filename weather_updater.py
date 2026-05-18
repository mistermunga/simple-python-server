import requests
import time
from threading import Timer

# Nairobi coordinates
NAIROBI_COORDINATES = (-1.2302285, 36.866615)

OPEN_METEO_API = "https://api.open-meteo.com/v1/forecast"

# Build API URL
LINK = (
    f"{OPEN_METEO_API}"
    f"?latitude={NAIROBI_COORDINATES[0]}"
    f"&longitude={NAIROBI_COORDINATES[1]}"
    f"&current=temperature_2m,weathercode"
    f"&timezone=Africa/Nairobi"
)

# Cache
weather_cache = {
    "data": None,
    "timestamp": None
}

REFRESH_INTERVAL = 3600  # 1 hour in seconds


def fetch_weather():
    """Fetch fresh weather data from API."""
    response = requests.get(LINK)
    response.raise_for_status()

    data = response.json()

    # Cache only relevant fields
    return {
        "temperature": data["current"]["temperature_2m"],
        "weathercode": data["current"]["weathercode"],
        "fetched_at": time.time()
    }


def update_weather():
    """Update cache with fresh data."""
    global weather_cache

    try:
        weather_cache["data"] = fetch_weather()
        weather_cache["timestamp"] = time.time()

        print(f"Updated: {weather_cache['data']['temperature']}°C")

        # Schedule next refresh in 1 hour
        Timer(REFRESH_INTERVAL, update_weather).start()

    except Exception as e:
        print("Weather fetch failed:", e)


def get_weather():
    """Return cached weather data."""
    return weather_cache["data"]