#count positives negatives and zero
numbers = [-5, 7, 9, -2, 0, 3, -8]
positive =0
negative=0
zero= 0
for num in numbers:
    if(num>0):
        positive+=1
    elif(num<0):
        negative+=1   
    else:
        zero+=1
print(positive)
print(negative)
print(zero)           