#WAP to print multiplication table of a given number ysing 'for' loop
n = int(input("Enter the number: "))
for i in range(1, 11): #here is 1 will be included and 11 won't be as included 
    print(f"{n} x {i} = {n * i}")
