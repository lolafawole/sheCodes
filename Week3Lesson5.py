def temp_converter(temperature, city):
    temperature = int(temperature)

    if temperature and city:
        temp_farenheit = (temperature * 9/5) + 32
        print(f"It is currently {temperature}ºC({temp_farenheit}ºF) in {city}")
    else: 
        print("Enter valid details")
        
temp_converter(15, "London")