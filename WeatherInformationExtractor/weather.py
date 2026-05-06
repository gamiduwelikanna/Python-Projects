from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Kansas City"):
    request_url = (
        f"http://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"
    )

    weather_data = requests.get(request_url).json()
    pprint(weather_data)
    return weather_data

if __name__ == "__main__":
    print('\n** Get current weather for Kansas City **\n')

    city = input("Please enter a city: ")
    weather_data = get_current_weather(city)

    print("\n")
    print("weather_data")
    