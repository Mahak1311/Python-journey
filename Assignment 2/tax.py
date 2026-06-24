'''Write a program that takes salary as input.
Using conditional statements,calculate the final tax rate based on these rules:
•If salary < 30,000 → 5%
•If salary is 30,000 – 70,000 → 15% 
•If salary > 70,000 → 25%'''
salary=int(input("Enter your salary: "))
tax=((5/100)*salary)
if(salary<300000):
    print("You have to pay 5% tax.\n The amount to be paid is:",tax)
elif(300000< salary< 700000):
    print("You have to pay 15% tax \n The amount to be paid is:",tax)
else:
    print("You have to pay 25% tax \n The amount to be paid is:",tax)    
