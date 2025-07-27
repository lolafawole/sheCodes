countries = {
  "Georgia": "Tbilisi",
  "Jamaica": "Kingston",
  "Albania": "Tirane"
}
print("Countries I'd like to visit: ")
# from solution:
# index = 0
# print(f"{index + 1}.{country} (Capital city: {capital})")
for i, (country, capital) in enumerate(countries.items(), start=1):
  print(f"{i}.{country} (Capital city: {capital})")