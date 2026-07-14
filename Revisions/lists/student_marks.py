#cal avg
marks = [75, 82, 91, 68, 55, 97, 84]
sums =0
for mark in marks:
    sums+=mark

avg=sums/len(marks)
print("Sum is: ", sums)    
print("avg is: ",avg)