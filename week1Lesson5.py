city = "London"
temperature_celcius = 16
temperature_farenhenheit = (temperature_celcius * 9 / 5) + 32
rounded_temperature_farenhenheit = round(temperature_farenhenheit)

print(
    f"The temperature in {city} is {temperature_celcius}C which is {rounded_temperature_farenhenheit}F"
)
