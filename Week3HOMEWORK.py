def farengheit_converter(temperature):
   farengheit_temperature = (temperature * 9/5) + 32
   return farengheit_temperature


city = input("Which city are you from?").capitalize()
temperature = float(input("What is the temperature in celcius?"))

print(f"It is currently {temperature}ºC({farengheit_converter(temperature)}ºF) in {city}")