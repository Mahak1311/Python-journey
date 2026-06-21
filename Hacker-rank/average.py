'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
 Print the average of the marks array for the student name provided, showing 2 places after the decimal.
 input format:
 The first line contains the integer n, the number of students' records. 
 The next n lines contain the names and marks obtained by a student,
each value separated by a space. The final line contains query_name, the name of a student to query.
'''
n = int(input())

students_marks = {}

for _ in range(n):
    data = input().split()

    name = data[0]
    marks = list(map(float,data[1:]))

    students_marks[name]= marks

query_name = input()
marks = students_marks[query_name]
average = sum(marks)/len(marks)
print(f"{average:.2f}")
