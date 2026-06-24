#Write a function to return the count the number of digits in a number. n
num= int(input("Enter any number: "))
count =0
while num>0:
    num=num//10 #removing last digit to count it
    count+=1
print(count)  
