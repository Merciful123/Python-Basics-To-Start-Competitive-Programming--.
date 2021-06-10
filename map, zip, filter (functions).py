##  Maping:-[1,2,3,4,5]   to  [1,4,9,16,25]

##  Firstly let's do it by coding, then by inbuild function.

square = []

numbers = [1,2,3,4,5]

for i in numbers:

    z = i*i

    square.append (z)

print ( "square:-" + "with code" + str ( square ) )


print("with function:-" + str ( list ( map ( lambda x:x*x, [1,2,3,4,5] ) ) ) )



##  concatenation of two lists:--



list1 = [1,2,3,4,5,6] 

list2 = [7,8,9,10,11] 

print ( list1 + list2 )




##  combining two lists as a tuple:--



print ( list ( zip ( list1,list2 ) ) )



##  filter:-filter elements in a list



print ( list ( filter ( lambda a:a%2 == 0,   [1,2,3,4,5,6,7,8,9,10,11,12,13] ) ) )