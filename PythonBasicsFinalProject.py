import requests
from rich import print
from datetime import datetime

print("[purple]Welcome to my Python weather app![/purple]")


city = input("Enter a city: ").strip().capitalize()
api_key = "73c0at20fo892f9e52b6b3bf1ca0b4f2"
api_url_weather = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"
api_url_forecast = f"https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}"

weather_response = requests.get(api_url_weather)
current_weather = weather_response.json()
forecast_response = requests.get(api_url_forecast)
current_forecast = forecast_response.json()


today_weather = round(current_weather["temperature"]["current"])
print(f"[blue]Today[/blue]: {today_weather}ºC")

print("[green]Forecast: [/green]")


for day in current_forecast['daily']:
  timestamp = day['time']  
  date = datetime.fromtimestamp(timestamp)
  formatted_day = date.strftime("%A")
  temperature = day['temperature']['day']
  print(f"{formatted_day}: {round(temperature)}ºC")
 

print("[yellow]Coded by Lola Fawole[/yellow]")




