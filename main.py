import google
from weather import WeatherForecast
from calculator import Calculator
from google import Googling
from imgconvert import ImageConverter
from youtdown import YoutubeDownloader

while True:
    try:
        print("Pick an app you want to use.")
        print("1 - Calculator")
        print("2 - Weather status")
        print("3 - Currency convertor - # not finished")
        print("4 - Timezone convertor- # not finished")
        print("5 - Google search")
        print("6 - Image convertor")
        print("7 - Youtube downloader")
        print("0 - Exits the program.")
        user_choice = int(input())

        if user_choice == 1:
            calculator = Calculator()
            calculator.calc_enabled()
        elif user_choice == 2:
            weather_forecast = WeatherForecast()
            weather_forecast.weather_mode()
        elif user_choice == 3:          # not finished
            pass
        elif user_choice == 4:          # not finished
            pass
        elif user_choice == 5:
            googling = Googling()
            googling.my_search()
        elif user_choice == 6:
            converter = ImageConverter()
            converter.convert_images_to_pdf()
        elif user_choice == 7:
            youtubeDownloader = YoutubeDownloader()
            youtubeDownloader.download()
        elif user_choice == 0:
            exit()
        else:
            print("Incorrect input.")
    except ValueError:
        print("Invalid input. Pick one of the options from the menu.")






