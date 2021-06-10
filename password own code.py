## Creating password generator:-

## ascii value  (A)-65 to (Z)-90

a = 'A'

print (ord(a)) 

import random

omit = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

letters = [chr(i) for i in range (35,125) if chr (i) not in omit]

random.choice (letters)

print ( random.choice (letters) )    ### will choose random chr( character whose unicode point is an integer.)

password = ""

length = int ( input ("enter the length") )

for i in range (0,length): 

    password =password + random.choice (letters)

print (password)


