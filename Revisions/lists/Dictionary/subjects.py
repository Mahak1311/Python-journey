student = {
    "Math":90,
    "Science":85,
    "English":92
}
print(student.keys()) #to print keys
print(student.values())#to print values
count = 0
for key, value in student.items():
    print(key, value) #to print both
    
for value in student.values():
    if value > 90:
        count += 1     #to count how many have 90+ marks

print(count) 
# find largest mark
largest = None
for value in student.values():
    if largest is None or value > largest:
        largest = value

print(largest)