## Creating Password Generator:--

a = 'A'

print ( ord(a) )

import random

omit = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

letters = [ chr(i) for i in range(65,90) if chr (i) not in omit ]

##  The chr() method returns a string representing a character whose Unicode code point is an integer.

random.choice ( letters )

print ( random.choice (letters) )   ### will choose random chr

password = ""

length = int ( input ("enter the length") )

for i in range ( 0, length ):

    password = password + random.choice ( letters )

print ( password )