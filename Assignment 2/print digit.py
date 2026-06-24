#Write a function that prints the of a number n ,digits
# For eg:n=312 there are 3 digits in it 3,1 and 2 & we need to print them.
a = int(input("Enter any number: "))

while a>0:
   last_digit=a%10
   print(last_digit)
   a=a//10 #float divide
    