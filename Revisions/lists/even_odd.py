#print even and odd in list
numbers = [12, 5, 18, 7, 20, 13, 4]
even=[]
odd=[]
for num in numbers:
    if(num%2==0):
        even.append(num)

    else:
       odd.append(num)

print(numbers)
print(even)
print(odd)