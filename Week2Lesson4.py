temperature = input("What is the temperature? ")
temperature = int(temperature)
rain = input("Is it raining? yes/no ")
rain = rain.upper()


if temperature >= 20 and rain == "NO":
    print("Enjoy sunny day!")
elif temperature >= 20 and rain == "YES":
  print("Don't forget your umbrella!")
elif temperature < 20 and rain == "NO":
  print ("Don't forget your jacket!")
else:
  print ("Don't forget your umbrella and your jacket!")