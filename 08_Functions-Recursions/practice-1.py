#WAP using function to find greatest of all three
a = int(input("Enter number-1: "))

b = int(input("Enter number-2: "))

c = int(input("Enter number-3: "))

def greatest(a, b, c): #this is "function definition"
    if(a>b and a>c):
        print("Number-1 is greatest!!")
    elif(b>a and b>c):
        print("Number-2 is greatest!!")
    else:
        print("Number 3 is greatest!!")
greatest(a, b, c)#this is "function calling"