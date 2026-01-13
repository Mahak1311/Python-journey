#Snake water gun game
'''
Information-
1 is for snake
-1 is for water
0 is for gun 
snake vs water: snake wins (1 vs -1)
water vs gun: water wins (-1 vs 0)
gun vs snake: gun wins (0 vs 1)
'''
import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "s", -1: "w", 0: "g"}

you = youdict[youstr]
print(f"You chose {reversedict[you]} and computer chose {reversedict[computer]} ")

if (computer==you):
    print("It's a draw")

elif(computer == 1 and you == -1):
 print("You lost :(")
elif(computer == 1 and you == 0):
 print("You won :)")
elif(computer == -1 and you == 1):
 print("You won :)")
elif(computer == -1 and you == 0):
 print("You lost :(")
elif(computer == 0 and you == -1):
 print("You won :)")
elif(computer == 0 and you == 1):
 print("You lost :(")

else:
 print("invalid input")