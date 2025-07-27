import requests

city = "Tokyo"
api_key = "73c0at20fo892f9e52b6b3bf1ca0b4f2"
api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

response = requests.get(api_url)

weather = response.json()

temperature = weather['temperature']['current']
country = weather['country']
humidity = weather['temperature']['humidity']

print(f"It is currently {temperature}ºC in {city}, {country} and the humidity level is {humidity}%")