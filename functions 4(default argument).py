## solving quadratic equation:-

import math 

def quadratic (b,c,a = 10):          ## non default argumnet follows default argument.

    determinant = math.sqrt (b * b - 4 * a * c)

    a1 = (-b-determinant) / (2*a*c)

    a2 = (-b+determinant) / (2*a*c)

    return a1, a2

a1, a2 = quadratic (b = 11,c = 3)

print ( "value a1:"+str (a1), "value a2:"+str (a2) )