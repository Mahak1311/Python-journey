#Temperature analysis
temps = [32, 35, 28, 40, 25, 38, 31]
largest= temps[0]
smallest= temps[0]
for temp in temps:
    if(temp>largest):
        largest=temp
    if(temp<smallest):
        smallest=temp    

print("Maximum temp: ",largest)
print("Minimum temp: ", smallest)