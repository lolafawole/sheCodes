# Create a dictionary of 3 countries you’d like to visit as a key and their capital city a value
countries = {
  "Georgia": "Tbilisi",
  "Jamaica": "Kingston",
  "Albania": "Tirane"
}
# Print out the dictionary
print(countries)
# Remove your least favorite country from the dictionary
countries.pop("Georgia")
# Print out the dictionary
print(countries)
# Add another country you'd like to visit 
countries["Finland"] = "Helsinki"
# Print out the dictionary
print(countries)
# Display the capital of each country (one at a time, don't use a loop)
print(countries["Jamaica"])
print(countries["Albania"])
print(countries["Finland"])