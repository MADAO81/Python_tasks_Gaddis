# The Marnrnal class represents a genus of mammals

class Mammal:
    
    # The init method takes an argument for the type of mammal.
    
    def __init__(self, species):
        self.__species = species 
        
    # The show_species method outputs a message about the type of mammal.
    
    def show_species(self):
        print("I am - ", self.__species)
        
    # The make_sound method emits a sound characteristic of all mammals.
    
    def make_sound(self):
        print("Arghhhhh")
 # The class Dog is a subclass of Mammal 
        
class Dog(Mammal):
    
    # __init__ method calls __init__ method of superclass, an advanced "dog" as a species
    
    def __init__(self):
        Mammal.__init__(self, "dog")
        
    # make_sound method overrides make_sound method of superclass
    
    def make_sound(self):
        print("Bow-wow-wow!")
        
# The Cat class is a subclass of the Mammalian class.

class Cat(Mammal):
    
    # The init method calls the init method of the superclass, passing 'cat' as the type.
    
    def __init__(self):
        Mammal.__init__(self, "cat")
        
    #  make_sound method overrides make_sound method of superclass
    def make_sound(self):
        print("Meow!")
        