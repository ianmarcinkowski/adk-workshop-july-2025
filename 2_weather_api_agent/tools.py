import requests


def get_weather_from_api(city: str) -> dict:
    """Retrieves the current weather report for a specified city.
    Args:
        city (str): The name of the city for which to retrieve the weather
            report.

    Returns:
        dict: status and result or error msg.
    """
    city = city.strip().lower()
    if not city:
        return {
            "status": "error",
            "error_message": "City name cannot be empty.",
        }

    # Use Open-Meteo Geocoding API to find coordinates for the city
    geocoding_url = (
        f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    )
    try:
        geo_response = requests.get(geocoding_url)
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return {
                "status": "error",
                "error_message": f"Could not find weather for '{city}'.",
            }

        location = geo_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        name = location["name"]

        # Use Open-Meteo Weather API to get the weather
        weather_url = (
            "https://api.open-meteo.com/v1/forecast?latitude="
            f"{latitude}&longitude={longitude}&current_weather=true"
        )
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current_weather = weather_data["current_weather"]
        temperature = current_weather["temperature"]
        wind_speed = current_weather["windspeed"]

        report = (
            f"The current weather in {name} is {temperature}°C with a "
            f"wind speed of {wind_speed} km/h."
        )

        return {"status": "success", "report": report}

    except requests.exceptions.RequestException as e:
        return {"status": "error", "error_message": f"API request error: {e}"}

