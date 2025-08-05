#WAP to print the star pattern for n=3
'''
  *
 * * *
* * * * *
'''
n = int(input("Enter number: "))
for i in range(1, n+1):
    print(" " * (n-i),end="")
    print("* "* i,end="")
    print("\n")