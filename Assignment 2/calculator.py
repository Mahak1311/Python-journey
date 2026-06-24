'''Letʼs create a Simple Calculator that performs arithmetic operations.
Create a function calculator(a, b, operation) that performs addition,subtraction,multiplication,or division based on the operation parameter.[parameter can have values +,-,*,/'''
def calculator(a,b,operation):
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    operation = input("Enter operation(+,-,*,/): ")

    if(operation=='+'):
     print(F"The answer is: {a+b}")

    elif(operation=='-'):
     print(F"The answer is: {a-b}")

    elif(operation=='*'):
     print(F"The answer is: {a*b}")
     
    if(operation=='/'):
     print(F"The answer is: {a//b}")

     
calculator(0, 0, '')

 