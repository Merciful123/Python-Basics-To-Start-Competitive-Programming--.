## Methods in Object Oriented Programming:-

class car:

    def __init__ (self,mileage,colour):

        self.mileage = mileage

        self.colour = colour

    def getmileage (self):

        return self.mileage

    def getcolour (self):

        return self.colour

    def greet (self):

        print ("hello i am a car")

model1 = car (60,"red") 

model2 = car (80,"white")

print ( model1.getmileage () )

print ( model2.getmileage () )

model2.greet ()

model1.greet ()