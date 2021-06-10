## Creating a Quadratic Equation:-

import math

def quadratic (a,b,c):

    determinant = math.sqrt (b**2-4*a*c)

    p1 = (-b+determinant) / 2*a*c

    p2 = (-b-determinant) / 2*a*c

    return p1,p2

p1 , p2 = quadratic (2, 32, 128)

print (p1, p2)

print ("p1:-" + str (p1) )

print ("p2:-" + str (p2) )