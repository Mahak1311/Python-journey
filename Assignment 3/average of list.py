#To find average in a list
n=int(input("How many numbers? "))
num=[]
for i in range(n):
    val=int(input("Enter values in list: "))
    num.append(val)

print(num)    
avg=sum(num)/len(num)
print(f"The avgerage of {num} is {avg}")