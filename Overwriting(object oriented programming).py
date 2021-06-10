##  By ineheritance we can make available the objects of other to another class:- example below

class animal:

    def __init__ ( self,colour ):

        self.colour = colour

    def introduce (self):

        print ( "i am an animal" )

    def makesound (self):

        print ( "making sound" )

class dog (animal):

    def makesound (self):

        print ( "bow bow" )

    def takecare (self):

        print ( "i am taking care of you" )

class cat (animal):

    def makesound (self):

        print ( "meow meow" )

wild_animal = animal ("red")

puppy = dog ("white")

kitten = cat ("white")
 
puppy. makesound ()

kitten. makesound ()