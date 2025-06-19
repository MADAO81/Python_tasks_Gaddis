# This program preserves CellPhone objects.
import pickle 
import cellphone 

# A constant for the file name.
FILENAME = "cellphones.dat"

def main():
    # initialize valuable for manage the loop
    again = "y"
    
    # open the file 
    output_file = open(FILENAME, "wb")
    
    # get the data from the user
    while again.lower() == "y":
        # Get cell phone data.
        man = input("Enter the manufacturer: ")
        mod = input("Enter the model number: ")
        retail = float(input("Enter the retail price: "))
        
        # create a CellPhone object 
        phone = cellphone.CellPhone(man, mod, retail)
        
        # Preserve the object and write it to a file.
        pickle.dump(phone, output_file)
        
        # Get another data item?
        again = input("Enter another data item? (y/n): ")
        
    # close file 
    output_file.close()
    print("The data is recorded in", FILENAME)
    
# call main function 
main()