"""api.py Put api calls here"""
import requests
from ipware import get_client_ip


def get_temperature(location):
    """get temperature of location from openweathermap"""
    APPID = "bf00ddf0cb365dae2d5f1ba1a15efaa9"
    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?units=metric&q=" +
            location+"&APPID="+APPID
        )  # Request weather data
        return response.json()["main"]["temp"]
    except:
        # Log error here
        return None


def get_geolocation_from_ip(request):
    """Attempt to infer location from ip"""
    # Navigator.geolocation is preferred method for getting location but requires a secure https context
    ip, _ = get_client_ip(request)
    url = f"http://api.ipstack.com/{ip}?access_key=fd46964a11969c9694a34763cd16a18a"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["city"]
