import requests
import urllib.parse


def get_weather_from_api(city: str) -> dict:
    """Retrieves the current weather report for a specified city.
    Args:
        city (str): The name of the city for which to retrieve the weather
            report.

    Returns:
        dict: status and result or error msg.
    """
    try:
        # Sanitize the city name
        city = city.strip()
        if not city:
            return {"status": "error", 
                    "message": "City name cannot be empty"}
        
        # URL encode the city name for safe API call
        city_encoded = urllib.parse.quote(city)
        
        # Make API call to wttr.in (free weather API, no token required)
        url = f"https://wttr.in/{city_encoded}?format=j1"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            weather_data = response.json()
            
            # Extract relevant information from the API response
            current = weather_data.get('current_condition', [{}])[0]
            location = weather_data.get('nearest_area', [{}])[0]
            
            result = {
                "city": location.get('areaName', [{}])[0].get('value', city),
                "country": location.get('country', [{}])[0].get('value', ''),
                "temperature_c": current.get('temp_C', ''),
                "temperature_f": current.get('temp_F', ''),
                "condition": (current.get('weatherDesc', [{}])[0]
                             .get('value', '')),
                "humidity": current.get('humidity', ''),
                "wind_speed_kmh": current.get('windspeedKmph', ''),
                "wind_direction": current.get('winddir16Point', ''),
                "feels_like_c": current.get('FeelsLikeC', ''),
                "feels_like_f": current.get('FeelsLikeF', '')
            }
            
            return {"status": "success", "result": result}
        else:
            error_msg = f"Failed to fetch weather data. Status code: {response.status_code}"
            return {"status": "error", "message": error_msg}
            
    except requests.RequestException as e:
        return {"status": "error", "message": f"Network error: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {str(e)}"}
