## complex number:- x+iy

## object oriented programming:-

class complexnumber:

    def __init__ (self,real,img):

        self.real = real

        self.img = img

    def __str__ (self):

        return "{} + {}i" .format (self.real,self.img)

    def __add__ (self,other):

         x = self.real + other.real

         y = self.img + other.img

         return "{} + {}i" .format(x,y)

num1 = complexnumber (4,5)

num2 = complexnumber (10,27)

print (num1+num2)