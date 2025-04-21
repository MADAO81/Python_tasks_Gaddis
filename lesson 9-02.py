# This program uses a dictionary to store the names and birthdays of friends.

# Global constants for menu
LOOK_UP = 1 
ADD = 2 
CHANGE = 3
DELETE = 4 
QUIT = 5

# Main function
def main():
    # create an empty dictionary
    birthdays = {}
    
    # initialize valuable for user's choice 
    choice = 0 
    
    while choice != QUIT:
        # get choosen menu item 
        choice = get_menu_choice()
        
        # process the selected action option
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)
            
# get_menu_choice function shows menu  and gets chosen option
def get_menu_choice():
    print()
    print("Friends and their birthdays")
    print("============================")
    print("1. Find birthday date")
    print("2. Add new birthday")
    print("3. Edit birthday")
    print("4. Delete birthday")
    print("5. Exit the program")
    print()
    
    # Get chosen option
    choice = int(input("Enter the chosen option: "))
    
    # check the selected option for validity
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter the chosen option: "))
        
    # return chosen option
    return choice 
    
# look_up function searches name in "birthdays" dictionary 
def look_up(birthdays):
    # Get the name you are looking for 
    name = input("Enter the name: ")
    
    # find it in the dictionary
    print(birthdays.get(name, "Not found"))
    
# "add" function adds new record to the "birthdays" dictionary 
def add(birthdays):
    # get the name and birthday
    name = input("Enter the name: ")
    bday = input("Enter the birthday: ")
    
    # If name doesn't exist, create it 
    if name not in birthdays: 
        birthdays[name] = bday 
    else: 
        print("This record is already exist.")
        
# "change" function modifies an existing record in "birthdays" dictionary 
def change(birthdays):
    # get the name you are looking for
    name = input("Enter the name: ")
    
    if name in birthdays:
        # Get new birthday
        bday = input("Enter the new birthday: ")
        
        # update the record 
        birthday[name] = bday
    else:
        print("This name is not foud.")
        
# "delete" function deletes the record from the "birthdays" dictionary
def delete(birthdays):
    name = input("Enter the name: ")
    
    #if the name is found, then delete this record
    if name in birthdays: 
        del birthdays[name]
    else:
        print("This name is not foud.")
        

# Call main function
main()


    