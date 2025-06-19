# This program uses function to create the list.
# This function returns link to list.

def main():
    # get list with values
    numbers = get_values()
    
    # Show values in list
    print("Numbers in list: ")
    print(numbers)
    
    
# get_values function receives numbers from user and saves it to the list
# this function returns link to list
def get_values():
    # create empty list
    values = []
    
    # create variable for cycle management
    again = "y"
    
    # get values from user and add it to list
    while again == "y" or again == "Y":
        # get value from user and add it to list
        num = int(input("Enter the number: "))
        values.append(num)
        
        # Repeat?
        print("Do you want to add one more number?")
        again = input("'y' = yes, all the rest = 'no'.")
        print()
        
    # return list
    return values


# call main function
main()

        