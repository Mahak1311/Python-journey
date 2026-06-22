# Break- To terminate the loop 
# Continue: To skip current iteration
i = 1
while(i <= 10):
    if(i == 8):
        break
    if(i == 4):
        i += 1
        continue
    print(i)
    i += 1

print("outside the loop...")
