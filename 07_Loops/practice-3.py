#WAP to check if a number is prime or not
a = int(input("Enter a number: "))

for i in range(2, a):
    if(a%i)==0:
     print("Number is not prime")
     break
    else:
     print("Number is prime")