# This program demonstrates the application of the append method to add a value to a list.

def main():
    # At first create empty list
    name_list = []
    
    # Create value to manage the loop
    again = "y"
    
    # Add some names to the list
    while again == "y" or again == "Y":
        # Get name from user
        name = input("Enter the name: ")
        
        # Add name to the end of the list
        name_list.append(name)
        
        # Add one more?
        print("Would you like to add one more name to the list?")
        again = input("y = yes, all the rest = no: ")
        print()
        
    # Show entered names 
    print("Here is the names, that you entered.")
    
    for name in name_list:
        print(name)
        
        
# call main function
main()