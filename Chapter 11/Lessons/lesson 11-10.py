# This program demonstrates polymorphism.

import animals

def main():
    # create an object of Mammal, object Dog and object Cat 
    mammal = animals.Mammal("Ordinary animal")
    dog = animals.Dog()
    cat = animals.Cat()
    
    # Show information about each animal.
    print("Here is some animals and ")
    print("sound, that they make.")
    print("-----------------------")
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    
# The show mama info function takes an object as an argument and calls its show_species and make sound methods.

def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()
    
# call main function
main()
        