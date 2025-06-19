# This program demonstrates "insert" method 

def main():
    # Create list with some names
    names = ["Ivan","Abram","Joseph", "Anna","Julia"]
    
    # Show list
    print("List before insert: ")
    print(names)
    
    # Insert new name to "0" element
    names.insert(0, "Evgeniy")
    
    # Show list again
    print("List after insert: ")
    print(names)


# call main function
main()