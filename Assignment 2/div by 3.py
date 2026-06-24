'''WAP to print all numbers from 1 to 100 which are divisible by both 3 and 5'''
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print(i)