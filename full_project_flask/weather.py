import requests
from dotenv import load_dotenv  # noqa
from pprint import pprint
import os
load_dotenv()


def get_current_weather(city="Lahore"):
    print('\n*** Get current Weather ****\n')

    # city = input('\n Please enter city name:\n')
    rquest_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    # print(rquest_url)
    weather_data = requests.get(rquest_url).json()
    # pprint(weather_data)
    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only spaces
    # This step is not required here
    # if not bool(city.strip()):
    #     city = "Kansas City"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
