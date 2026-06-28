#To check if string is palindrome or not (eg: madam,racecar)
word = input("Enter any string: ")
word = word.strip()
start = 0
end = len(word) - 1
is_palindrome = True
while start < end: #using two pointer approach
    if word[start] != word[end]:
        is_palindrome = False
        break
    start += 1
    end -= 1

if is_palindrome:
    print("A palindrome")
else:
    print("Not a palindrome")
