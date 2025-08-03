#To detect spam comments
a = input("Enter your comment: ")
if("Make a lot of money" in a):
    print("This is a spam comment")
elif("Buy now" in a):
    print("This is a spam comment")
elif("Subscribe this" in a):
    print("This is a spam comment")
elif("Click this" in a ):
    print("This is a spam comment")
else:
    print("Your comment is good to go!!")