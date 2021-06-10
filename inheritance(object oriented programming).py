## By ineheritance we can make available the objects of other

# In objects of other class :-inheritance (think)

class animal:

    def __init__ (self,colour):

        self.colour = colour

    def introduce (self):

        print ( "i am an animal" )

    def makesound (self):

        print ( "making sound" )

class dog (animal):

    def makesound (self):

        print("bow bow")

    def takecare (self):

        print ( "i am taking care of you" )

wild_animal = animal ( "brown" )

puppy = dog ( "white" )

wild_animal.makesound()    ## Object is used to call a method

puppy.introduce()         
 