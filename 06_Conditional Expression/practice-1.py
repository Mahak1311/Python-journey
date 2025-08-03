#To find greatest of four number entered by user
a = int(input("Enter numner-1: "))
b = int(input("Enter numner-2: "))
c = int(input("Enter numner-3: "))
d = int(input("Enter numner-4: "))
if(a>b and a>c and a>d):
    print("Number 1 is the greatest")
elif(b>a and b>c and b>d):
    print("Number 2 is the greatest")
elif(c>a and c>b and c>d):
    print("Number 3 is the greatest")
else:
    print("Number 4 is the greatest")

