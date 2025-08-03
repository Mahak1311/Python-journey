#To input 8 numbers from the user and display all unique numbers

s = set()
num = int(input("Enter number 1: "))
s.add(int(num))
num = int(input("Enter number 2: "))
s.add(int(num))
num = int(input("Enter number 3: "))
s.add(int(num))
num = int(input("Enter number 4: "))
s.add(int(num))           
num = int(input("Enter number 5: "))
s.add(int(num))
num = int(input("Enter number 6: "))
s.add(int(num))
num = int(input("Enter number 7: "))
s.add(int(num))
num = int(input("Enter number 8: "))
s.add(int(num))

print("Here you go: ",s) #As set doesn't repeat items it is useful to print unique numbers