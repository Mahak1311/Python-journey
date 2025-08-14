#WAP using function to convert fahrenheit to celsius
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
print(f_to_c(f))