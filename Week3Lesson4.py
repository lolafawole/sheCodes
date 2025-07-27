"""Super useful function that shows what the current weather conditions are in your city"""

def weather_app(city, temperature, humidity=""):
    
    if humidity:
        city = city.capitalize()
        print(f"The temperature in {city} is {temperature} degrees with a humidity of {humidity}.")
    else:
        city = city.capitalize()
        print(f"The temperature in {city} is {temperature} degrees")
        
weather_app("london", 22, 49)
weather_app("paris", 23)