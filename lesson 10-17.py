# This program will reactivate CellPhone objects.
import pickle
import cellphone 

# A constant for the file name.
FILENAME = "cellphones.dat"

def main():
    end_of_file = False # To indicate the end of the file
    
    # open the file 
    input_file = open(FILENAME, "rb")
    
    # read file to the end 
    while not end_of_file:
        try:
            # Reactivate the next object.
            phone = pickle.load(input_file)
            
            # Show cell phone data.
            display_data(phone)
        except EOFError:
            # Set a flag to indicate that the end of the file has been reached.
            end_of_file = True 
            
    # close the file 
    input_file.close()
    
# The display_data function shows the data from the CellPhone object passed as an argument.
def display_data(phone):
    print("Manufacturer: ", phone.get_manufact())
    print("Model number: ", phone.get_model())
    print("Retail price: $", format(phone.get_retail_price(), ",.2f"), sep="")
    print()
    
# call main function
main()