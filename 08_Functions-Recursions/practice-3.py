#Sum of first n numbers using recurssion
n = int(input("Enter value of number: "))
def sum(n):
    if(n==1):
      return 1
    return sum(n-1) + n
print(sum(n))