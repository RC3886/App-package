import requests                              # request url
import datetime                              # converts/formats sunset/sunrise from Unix to a readable form
# possible update - use geocoder to detect current city?


class WeatherForecast:                        # default place is my town to ease the app use, but can be changed
    def __init__(self, city="Lipnik nad Becvou", country_code="CZ", api_key="2c670ab99c6f13157d82a0ec8d714c22"):
        self.city = city
        self.country_code = country_code
        self.api_key = api_key
        self.weather_data = None                     # default to none,so if the result is none, something is wrong

    def get_weather(self):                           # get json from openweathermap.com
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city},{self.country_code}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        self.weather_data = response.json()

    def get_temperature(self):
        return self.weather_data["main"]["temp"]

    def get_feels_like(self):
        return self.weather_data["main"]["feels_like"]

    def get_wind_speed(self):
        return self.weather_data["wind"]["speed"]

    def get_humidity(self):
        return self.weather_data["main"]["humidity"]

    def get_description(self):
        return self.weather_data["weather"][0]["description"]

    def get_sunrise_time(self):
        sunrise_unix = self.weather_data["sys"]["sunrise"]      # Unix, repr. the number of seconds since Jan 1, 1970
        sunrise_time = datetime.datetime.fromtimestamp(sunrise_unix)    # converted to a readable form
        return sunrise_time.strftime("%H:%M")                           # more simple format

    def get_sunset_time(self):
        sunset_unix = self.weather_data["sys"]["sunset"]        # Unix, repr. the number of seconds since Jan 1, 1970
        sunset_time = datetime.datetime.fromtimestamp(sunset_unix)  # converted to a readable form
        return sunset_time.strftime("%H:%M")                        # more simple format

    def weather_status_complete(self):
        print(f"The current weather in {self.city} is: ")
        print(f"Temperature is {self.get_temperature()}°C, feels like {self.get_feels_like()}°C, {self.get_description()}.")
        print(f"Wind speed is {self.get_wind_speed()}m/s, humidity {self.get_humidity()}%.")
        print(f"The Sun rises at {self.get_sunrise_time()} and sets at {self.get_sunset_time()}.")

    def weather_mode(self):
        weather_mode_enabled = True
        while weather_mode_enabled:
            self.get_weather()
            self.weather_status_complete()
            weather_input = int(input("If you wish to change the location, press 1, press 2 to go back to the app menu."))
            if weather_input == 1:
                self.city = str(input("Enter a city: "))
                self.country_code = str(input("Enter a country code: "))
            elif weather_input == 2:
                weather_mode_enabled = False






