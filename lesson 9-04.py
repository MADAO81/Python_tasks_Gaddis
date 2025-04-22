# This program demonstrates the conservation of objects
import pickle

# main function
def main():
    again = "y" # for control the repetition of the cycle
    
    # open file to binary record
    output_file = open("info.dat", "wb")
    
    # get data until the user decides to stop.
    while again.lower() == "y":
        # get data about person and save it 
        save_data(output_file)
        
        # Does the user want to enter more data?
        again = input( "Would you like to enter more data? (y/n): ")
        
    # close file 
    output_file.close()
    
    
# The save_data function gets data about a person, 
# saves them in the dictionary and then
# saves the dictionary in the specified file.
def save_data(file):
    # create an empty dictionary
    person = {}
    
    # get data for person and save it to the dictionary
    person["name"] = input("Name: ")
    person["age"] = int(input("Age: "))
    person["mass"] = float(input("Mass: "))
    
    # conservate file
    pickle.dump(person, file)
    
# call main function
main()
    
