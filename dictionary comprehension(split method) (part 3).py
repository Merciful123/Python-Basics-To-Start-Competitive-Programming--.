##  Dictionary comprehension  ( Concepts ) :---

## sentence:-input, key:-word,  value:-length of words

sentence = input ("enter the sentence")

z = sentence.split (" ")     ## split :-provides us words in list

print ( z )         

a = { z:len(z) for z in z }
 
print (a)
