#Take input of two list and merge them and sort it
size = int(input("How many elements in list 1? "))
n=[]
for i in range(size):
    num=int(input("Enter number for list 1: "))
    n.append(num)

sizes=int(input("How many elements for list 2? "))  
m=[]
for i in range(sizes):
    nums=int(input("Enter elements for list 2: "))
    m.append(nums)

print(f"List 1: {n}")
print(f"List 2: {m}")

p=n+m
print(sorted(p))     