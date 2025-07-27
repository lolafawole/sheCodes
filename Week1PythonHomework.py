name = input("What is your name? ")
city = input("Where are you currently located? ")
temperature = input("What is the temperature in Celsius: ")
temp_celsius = float(temperature)  
temp_fahrenheit = (temp_celsius * 9/5) + 32
print(f"Hi {name}, you are in {city}, and it is currently {temp_celsius}ºC or {temp_fahrenheit}ºF")
print(f"I predict that tonight, the temperature will reach {temp_celsius - 10}ºC or {temp_fahrenheit -20}ºF")
print ("Have a good day!")