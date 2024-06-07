import requests
import os

def get_weather_api(event, context):
    # Openweather API key
    api_key = os.getenv('openweather_api')
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    CITY = "Berlin"
    url = f'{BASE_URL}appid={api_key}&q={CITY}'
    
    response = requests.get(url).json()
    
    return response