#to write a table of number
def table(n):
    for i in range(1, 11):
      print(f"{n} x {i} = {n*i}")
n = int(input("Enter value of n: "))      
table(n)