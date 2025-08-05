#WAP to greet all the person name stored in a list 'l' and which starts with 'S'
print("Enter 5 names!!")
l = []
n1 = input("Enter name of person-1: ")
l.append(n1)
n2 = input("Enter name of person-2: ")
l.append(n2)
n3 = input("Enter name of person-3: ")
l.append(n3)
n4 = input("Enter name of person-4: ")
l.append(n4)
n5 = input("Enter name of person-5: ")
l.append(n5)

print(l)
for name in l:
 if(name.strip().lower().upper().startswith("S")): 
    '''used strip,lower and upper 
    so if the names have space or written in uppercase or lowers case the loop will still run'''
    print(f"Hello {name}")
print("Doneee")     