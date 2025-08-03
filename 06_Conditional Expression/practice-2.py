#Find out whether a student has passed or failed if it requires total of 40% and atleast 33% in each subject to pass.
M1 = int(input("Enter your marks in subject-1: "))
M2 = int(input("Enter your marks in subject-2: "))
M3 = int(input("Enter your marks in subject-3: "))
total_percentage = (100*(M1 + M2 + M3)/300)

if(total_percentage>40 and M1>33 and M2>33 and M3>33):
    print(f"You passed with {total_percentage}%")
else:
    print(f"You failed with {total_percentage}%")    

