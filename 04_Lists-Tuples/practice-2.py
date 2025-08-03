#To accept marks from 6 students and display them in a sorted manner
Marks = []
m1 = int(input("Enter Marks of Student 1:"))
Marks.append(m1)
m2 = int(input("Enter Marks of Student 2:"))
Marks.append(m2)
m3 = int(input("Enter Marks of Student 3:"))
Marks.append(m3)
m4 = int(input("Enter Marks of Student 4:"))
Marks.append(m4)
m5 = int(input("Enter Marks of Student 5:"))
Marks.append(m5)
m6 = int(input("Enter Marks of Student 6:"))
Marks.append(m6)
sort = Marks.sort() #Sorts the items in the list
print(Marks)