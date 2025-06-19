# This program tests the CellPhone class

import cellphone 

def main(): 
    # get phone info 
    man = input("Enter the manufacturer: ")
    mod = input("Enter the model number: ")
    retail = float(input("Enter the retail price: "))
    
    # Create an instance of the CellPhone class.
    phone = cellphone.Cellphone(man, mod, retail)
    
    # Show entered info 
    print("Here is the data you entered: ")
    print("Manufacturer: ", phone.get_manufact())
    print("Model number: ", phone.get_model())
    print("Retail price: $", format(phone.get_retail_price(), ".2f", sep = ""))
    
# call main function 
main()