## sorting

## list of tuple pairs 

list1 = [ (38,2), (3,10), (5,1), (30,8) ]

print ( "sorted on the order of ist element" )

print (sorted (list1) )

## on the order of first element:-

print ( "sorted on the order of second element" )

print ( sorted (list1, key=lambda x:x[1])  )