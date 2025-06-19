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
    print()
    show_mammal_info("Bababuweeee-Bababuweeee-Bababuweeee")
    
# The show mama info function takes an object as an argument and calls its show_species and make_sound methods.

def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print("It is not a  mammal!")
    
# call main function
main()
        