#create a dict which maps word to it's length
words=["apple","banana","kiwi","cherry","mango"]
dict={}
for val in words:
    dict[val]=len(val)
print(dict)    