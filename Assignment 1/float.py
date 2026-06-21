'''Ask the user to enter two integers and one float.
Convert them all to floats and print their average.'''
print("Enter 2 integers and 1 float!")
a = int( input("Enter integer 1: "))
a1 = float(a)
print(a1)
b = int(input("Enter integer 2: "))
b1 = float(b)
print(b1)
c = float(input("Enter float number: "))
avg = float((a+b+c)/3)
print("The average is: ",avg)