#to print the star pattern
'''
  *
 * * 
* * *
'''
def pattern(n , limit):
     if n>limit: #limit is there so the code knows when to stop
       return #return is there to make sure that if "if" condition is satisfied below code doesn't run
     print("* " * n)
     pattern(n+1, limit) 

pattern(1,4)
'''
* * * * *
 * * * *
  * * *
   * *
    *
'''

def patterns(x):
    if(x==0):
     return
    print("* " * x)
    patterns(x-1)
patterns(5)   