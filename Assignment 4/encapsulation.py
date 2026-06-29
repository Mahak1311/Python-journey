#private sttributes and getter setter with validation
class Student:

    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    # Getters
    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks

    # Setters
    def set_name(self, new_name):
        if new_name == "":
            print("Name cannot be empty")
        else:
            self.__name = new_name

    def set_roll_no(self, new_roll):
        if new_roll <= 0:
            print("Invalid roll number")
        else:
            self.__roll_no = new_roll

    def set_marks(self, new_marks):
        if new_marks < 0 or new_marks > 100:
            print("Invalid marks")
        else:
            self.__marks = new_marks

name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

s1 = Student(name, roll_no, marks)

while True:

    print("\n1. Display Student Details")
    print("2. Update Name")
    print("3. Update Roll Number")
    print("4. Update Marks")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Name:", s1.get_name())
        print("Roll No:", s1.get_roll_no())
        print("Marks:", s1.get_marks())

    elif choice == 2:
        new_name = input("Enter new name: ")
        s1.set_name(new_name)
        print(f"Updated name: {new_name}")

    elif choice == 3:
        new_roll = int(input("Enter new roll number: "))
        s1.set_roll_no(new_roll)
        print(f"Updated roll no: {new_roll}")

    elif choice == 4:
        new_marks = float(input("Enter new marks: "))
        s1.set_marks(new_marks)
        print(f"Updated marks: {new_marks}")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice")