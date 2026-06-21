'''WAP to swap values of two numbers entered by the user.'''
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
temp = a #temp variable to store value of a
a = b 
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)