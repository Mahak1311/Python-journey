#Inheritance
class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):

    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats


class Bike(Vehicle):

    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc


# Car Input
car_brand = input("Enter car brand: ")
car_model = input("Enter car model: ")
seats = int(input("Enter number of seats: "))

# Bike Input
bike_brand = input("Enter bike brand: ")
bike_model = input("Enter bike model: ")
engine_cc = int(input("Enter engine CC: "))

# Objects
c = Car(car_brand, car_model, seats)
b = Bike(bike_brand, bike_model, engine_cc)

# Output
print("\nCar Details")
print("Brand:", c.brand)
print("Model:", c.model)
print("Seats:", c.seats)

print("\nBike Details")
print("Brand:", b.brand)
print("Model:", b.model)
print("Engine CC:", b.engine_cc)

