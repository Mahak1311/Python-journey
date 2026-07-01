import json


cities = {
    "Dholakpur":"2000",
    "Toonpur":"4000",
    "Zootopia":"150000"
}

with open("C:\\Users\\mahak\\Python-journey\\Assignment 5\\cities.json", "w") as file:
    json.dump(cities, file)


with open("C:\\Users\\mahak\\Python-journey\\Assignment 5\\cities.json", "r") as file:
    data = json.load(file)

print("Cities and Populations:")

for city, population in data.items():
    print(city, ":", population)


new_city = input("Enter new city: ")
new_population = int(input("Enter population: "))

data[new_city] = new_population


with open("C:\\Users\\mahak\\Python-journey\\Assignment 5\\cities.json", "w") as file:
    json.dump(data, file)

print("\nUpdated Data:")

with open("C:\\Users\\mahak\\Python-journey\\Assignment 5\\cities.json", "r") as file:
    updated_data = json.load(file)

for city, population in updated_data.items():
    print(city, ":", population)