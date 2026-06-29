#overriding area
class Shape:

    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


radius = float(input("Enter radius: "))
length = float(input("Enter length: "))
width = float(input("Enter width: "))
base = float(input("Enter base: "))
height = float(input("Enter height: "))

c = Circle(radius)
r = Rectangle(length, width)
t = Triangle(base, height)

print("Area of Circle =", c.area())
print("Area of Rectangle =", r.area())
print("Area of Triangle =", t.area())