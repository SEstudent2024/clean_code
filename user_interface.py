from weather_data_fetcher import WeatherDataFetcher
from data_parser import DataParser

class UserInterface:
    def __init__(self):
        self.weather_fetcher = WeatherDataFetcher()
        self.parser = DataParser()

    def display_weather(self, city):
        """Display basic weather forecast for a city."""
        data = self.weather_fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse_weather_data(data)
            print(weather_report)

    def get_detailed_forecast(self, city):
        """Provide detailed weather forecast for a city."""
        data = self.weather_fetcher.fetch_weather_data(city)
        return self.parser.parse_weather_data(data)

    def start(self):
        """Start the user interface for weather forecast application."""
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
                print(forecast)
            else:
                self.display_weather(city)