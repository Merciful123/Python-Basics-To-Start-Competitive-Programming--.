## Creating an object of a class called :-instantiation.

## In other words we can say instantiating a class.

class students:

    def __init__ (self,name,age): ##  constructor definition

        self.sname = name

        self.sage = age

        print ("my name is {} and my age is {}".format (self.sname,self.sage) )

        ##  self will refer to the current object
         
student1 = students ("Aamir",25)

student2 = students ("Noor",28)

##  object name = class name()

student3 = students ("Danish",22)

student4 = students ("qruzz",23)

print ( student4.sage )

print( student2.sname )

print( student3.sage )

print( student4.sname )




