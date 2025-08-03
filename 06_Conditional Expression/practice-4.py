# to check if username has less than 10 characters or not
a = input("Enter your username: ")
if(len(a)<10):
    print("This username has less than 10 characters.")
elif(len(a)==10):
    print("This username contains exactly 10 characters.")
else:
    print("This username has more than 10 characters")