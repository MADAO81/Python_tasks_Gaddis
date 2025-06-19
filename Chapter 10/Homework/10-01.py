# import pet 
from objects import pet # the class is stored in objects folder

def main():
    # local valuables 
    pet_name = ""
    pet_type = ""
    pet_age = 0
    
    # get the information about pet 
    pet_name = input("Enter the name of pet: ")
    pet_type = input("Enter the type of pet: ")
    pet_age = int(input("Enter the age of pet: "))
    
    # Create an instance of the Pet class.
    mypet = pet.Pet(pet_name, pet_type, pet_age)
    
    # Show the entered info 
    print("Here is the data that you entered: ")
    print("Name of pet: ", mypet.get_name())
    print("Type of pet: ", mypet.get_animal_type())
    print("Age of pet: ", mypet.get_age())
    
# call main function
main()