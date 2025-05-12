# This program creates five CellPhone objects and saves them in a list.

import cellphone 

def main():
    # Get a list of CellPhone objects.
    phones = make_list()
    
    # show data in list 
    print("Here is the data you entered: ")
    display_list(phones)
    
# The make_list function receives data about five phones 
# from the user, and then returns a list of CellPhone objects containing this data.

def make_list():
    # create an empty list
    phone_list = []
    
    # add five objects CellPhone to the list 
    print("Enter the information about the five phones.")
    for count in range(1, 6):
        # Get phone information.
        print("Phone number "  + str(count) + ":")
        man = input("Enter the manufacturer: ")
        mod = input("Enter the model number: ")
        retail = float(input("Enter the retail price: "))
        print()
        
        # create a new object CellPhone in memory and assign it to the phone variable.
        phone = cellphone.CellPhone(man, mod, retail)
        
        phone_list.append(phone)

    # return the list 
    return phone_list 
    
# The display_list function takes a list with CellPhone 
# objects as an argument and shows the data stored in each object.

def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()
        
# call main function
main()
    