'''Design a program to continuously input a number n from user
 & print if it is positive or negative until the user enters “Quit” '''
while True:
    num = input("Enter numbers and to stop enter quit: ")

    if num=="quit": 
        break
    num =int(num)
        
    if num<0:
        print(f"{num} is negative \n ")
                
    elif num==0:
        print(f"{num} is equal to zero \n ") 

    else:
        print(f"{num} is positive \n") 
            
       
        



