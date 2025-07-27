city = input("Which city are you in? ")
temperature = input("What is the temperature? ")
if city and temperature:
  temperature = int(temperature)
  city = city.capitalize()

  if temperature > 20:
    print(
        f"It is currently warm in {city} with a temperature of {temperature}ºC"
    )
  elif temperature > 10:
    print(
        f"It is currently chilly in {city} with a temperature of {temperature}ºC"
    )
  elif temperature < 10:
    print(
        f"It is currently cold in {city} with a temperature of {temperature}ºC"
    )
else:
  print("Please try again and enter a city and temperature")
