class Herbivore:

    def eat_plants(self):
        print("Eats plants")

class Carnivore:

    def eat_meat(self):
        print("Eats meat")

class Omnivore:

    def eat_both(self):
        print("Eats both plants and meat")

class Bear(Herbivore, Carnivore, Omnivore):

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Bear Name:", self.name)


name = input("Enter bear name: ")

b = Bear(name)

b.display()
b.eat_plants()
b.eat_meat()
b.eat_both()