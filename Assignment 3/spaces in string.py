#number of spaces in string
word=input("Enter any string: ")
count=0
for ch in word:
   if(ch==" "):
      count+=1

print(count)