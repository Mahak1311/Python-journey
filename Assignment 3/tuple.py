#tuple of odd number and tuple of even number
size = int(input("Enter how many elements? "))
n = []
for i in range(size):
    num=int(input("Enter elements: "))
    n.append(num)

t=tuple(n)

even = []
odd = []

for num in t:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

even_tuple = tuple(even)
odd_tuple = tuple(odd)

print("Original tuple:", t)
print("Even tuple:", even_tuple)
print("Odd tuple:", odd_tuple)   
