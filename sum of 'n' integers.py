## sum of integers from '1' to 'n' without loop

n = int ( input ( "enter a number:-" ) ) 

print ( sum (list (range (1,n+1) ) ) )

## sum:- with loop

print ("with loop")

sum = 0

for i in range (1,n+1):

    sum+=i   ## sum = sum+i

print (sum)
