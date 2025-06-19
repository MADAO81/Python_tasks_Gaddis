# This program demonstrates the deconservation of objects.
import pickle

# main function 
def main():
    end_of_file = False # to indicate the end of the file
    
    # open file fot binary read 
    input_file = open("info.dat", "rb")
    
    # read file to the end 
    while not end_of_file:
        try:
            # deconservate next object 
            person = pickle.load(input_file)
            
            # show object
            display_data(person)
        except EOFError:
            # Set a flag to indicate that the end of the file has been reached.
            end_of_file = True 
            
    # close file 
    input_file.close()
    
# The display_data function shows data about a person in the dictionary that is passed as an argument.
def display_data(person):
    print("Name: ", person ["name"])
    print("Age: ", person["age"])
    print("Mass: ", person["mass"])
    print()
    
# call main function
main()