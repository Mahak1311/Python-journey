#WAF to return the sum of digits of a number,n.
num = int(input("Enter any number: "))

def sum(num):
    add=0
    while num>0:
        lastdigit=num%10
        num=num//10
        add+=lastdigit

    return add     
print(sum(num))
         
