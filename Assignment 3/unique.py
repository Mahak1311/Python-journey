#to print unique characters and their count
s = input("Enter a string: ")

unique_chars = set(s)

for ch in unique_chars:
    print(ch)

print("Count =", len(unique_chars))