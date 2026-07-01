import os
with open("C:\\Users\\mahak\\Python-journey\\Assignment 5\\names.txt", "w") as file:

    for i in range(5):
        name = input("Enter a name: ")
        file.write(name + "\n")

with open("C:\\Users\\mahak\\Python-journey\\Assignment 5\\names.txt", "r") as file:

    print("\nNames stored in file:")
    print(file.read())