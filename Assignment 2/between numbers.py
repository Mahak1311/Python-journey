'''Write a function that takes two integers a and b and prints all even numbers between them(inclusive)'''
a = int(input("Enter number 1: "))
b= int(input("Enter number 2: "))
for i in range(a,b+1): #as b is to included b+1 will be taken as range coz last number in range is not included
    if(i%2==0):
        print(f"{i} is even")
