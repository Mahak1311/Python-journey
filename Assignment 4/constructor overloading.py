class Person:

    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)

        if self.age is not None:
            print("Age:", self.age)

        if self.address is not None:
            print("Address:", self.address)


name = input("Enter name: ")

age = input("Enter age: ")
address = input("Enter address: ")

if age == "":
    p = Person(name)

elif address == "":
    p = Person(name, int(age))

else:
    p = Person(name, int(age), address)

p.display()