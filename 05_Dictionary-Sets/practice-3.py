# Create a fake dictionary and allow 4 friends to enter their fav language as value and use key as their names.
Dict = {}
name = input("Enter your name: ")
lang = input("Enter your fav language: ")
Dict.update({name:lang})
name = input("Enter your name: ")
lang = input("Enter your fav language: ")
Dict.update({name:lang})
name = input("Enter your name: ")
lang = input("Enter your fav language: ")
Dict.update({name:lang})
name = input("Enter your name: ")
lang = input("Enter your fav language: ")
Dict.update({name:lang}) #.update is used to add more items in a dictonary
print(Dict)