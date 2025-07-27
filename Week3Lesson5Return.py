def farengheit_converter(temperature):
   farengheit_temperature = (temperature * 9/5) + 32
   return farengheit_temperature


city = "London"
temperature = 15

print(f"It is currently {temperature}ºC({farengheit_converter(15)}ºF) in {city}")


    