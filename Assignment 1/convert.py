'''The user enters a string containing a number (e.g."45",).
Convert it to:
•an integer
•a float
•a string again 
Print all three values with their types.'''
num = input("Enter any number: ")
a = int(num)
print("The number converted into integer is: " , a)
print("The type is: " ,type(a))
b = float(num)
print("The number converted into float is: ",b)
print("The type is: ", type(b))
print("The number in string is: ",num)
print("The type is: ", type(num))
