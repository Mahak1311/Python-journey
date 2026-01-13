import random

n = random.randint(1,100)

a = -1
guesses = 0

while(a!=n):
    guesses +=1
    a = int(input("Enter any number of your choice: "))
    
    if(a>n):
        print("Lower your value")
    elif(a<n):
        print("Higher your value")
    else:
        print(f"You have guessed it correctly in {guesses} trials")