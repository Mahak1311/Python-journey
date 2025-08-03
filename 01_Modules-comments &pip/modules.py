#modules.py

'''
A module is a file containing code written by somebody 
else which can be imported and used in our programs.
'''
import pyjokes  
#Here pyjokes is a MODULE made by someone else and used by me.
joke = pyjokes.get_joke()
print(joke) 