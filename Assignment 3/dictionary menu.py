'''Create a dictionary where:
•Keys=student names
•Values=marks(integer)
Write a menu-based program where user presses a key(ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ)
depending on the operation they want to perform on the dictionary
'''

size=int(input("How many values? "))
dict = {}
for i in range(size):
    name=input("Enter student's name: ")
    marks=float(input("Enter student's marks: "))
    dict.update({name:marks})
print(dict)

operation = input("Enter operation \n (1.A-Add a student \n 2.B-Update marks \n 3.C-Search for a student\n 4.D-Display all students and marks) :")

if(operation=='A'):
    add=input("Insert Student's name: ")
    dict[add]=None
    print(dict)

elif(operation=='B'):
    student=input("Enter name of students whose marks you want to update: ")
    new_marks=float(input("Enter new marks: "))
    dict.update({student:new_marks})
    print(f"Updated dictionary: {dict}")

elif(operation=='C'):
    search = input("Enter name: ")
    if search in dict:
        print(dict[search])
    else:
        print("Student not found")

elif(operation=='D'):
    dict.items()
    print(dict)

else:
    print("Invalid operation")