# this program manage contacts
import contact
import pickle

# global constants for menu navigation
LOOK_UP = 1 
ADD = 2
CHANGE = 3 
DELETE = 4
QUIT = 5

# Global constant for the file name
FILENAME = "contacts.dat"

# main function 
def main():
    # load the existing dictionary of contacts and assign it to the my contacts variable.
    my_contacts = load_contacts()
    
    # initialize valuable for user's choice
    choice = 0
    
    # Process the menu options until the user wants to exit the program.
    while choice != QUIT:
        # Get the menu item selected by the user.
        choice = get_menu_choice()
        
        # process the selected option 
        if choice == LOOK_UP:
            look_up(my_contacts)
        elif choice == ADD:
            add(my_contacts)
        elif choice == CHANGE:
            change(my_contacts)
        elif choice == DELETE:
            delete(my_contacts)
            
    # Save the mycontacts dictionary to a file.
    save_contacts(mycontacts)

def load_contacts():
    try:
        # open file contacts.dat 
        input_file = open(FILENAME, "rb")
        
        # deconservate file 
        contact_dct = pickle.load(input_file)
        
        # close file phone_inventory.dat 
        input_file.close()
    except IOError:
        # couldn't open the file, so create an empty dictionary
        contact_dct = {}
    
    # return dictionary
    return contact_dct
    
# The "get_menu_choice" function displays a menu and receives a verified user-selected item.
def get_menu_choice():
    print()
    print("Menu")
    print("==============================================================")
    print("1.Find contact")
    print("2.Add new contact")
    print("3.Change existing contact")
    print("4.Delete contact")
    print("5.Exit the program")
    print()
    
    # Get chosen menu option 
    choice = int(input("Enter the chosen option: "))
    
    # check the selected item for validity
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter the chosen option: "))
        
    # return chosen option
    return choice
    
# look_up function searches the element in dictionary
def look_up(mycontacts):
    # Get the name you are looking for 
    name = input("Enter the name: ")
    
    # search it in the dictionary
    print(mycontacts.get(name, "This name is not found."))
    
# "add" function adds new record to the dictionary
def add(mycontacts):
    # get contact information 
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email: ")
    
    # create record whith "Contact" object 
    entry = contact.Contact(name, phone, email)
    
    # If the name does not exist in the dictionary, then add it as a key with its associated value as an object.
    if name not in mycontacts:
        mycontacts[name] = entry
        print("Record added")
    else:
        print("This name is already exist.")
        
# "change" function changes existed record in the dictionary
def change(mycontacts):
    # get the name you are looking for 
    name = input("Enter the name: ")
    
    if name in mycontacts:
        # get the new phone number
        phone = input("Enter the new phone number: ")
        # get the new email 
        email = input("Enter the new email: ")
        
        # Create the new record with "Contact" object
        entry = contact.Contact(name, phone, email)
        
        # update the record
        mycontacts[name] = entry 
        print("Information updated.")
    else:
        print("This name is not found.")
        
# "delete" function deletes the entry off the dictionary
def delete(mycontacts):
    # get the name you are looking for 
    name = input("Enter the name: ")
    
    # If name is finded, then delete the entry 
    if name in mycontacts:
        del mycontacts[name]
        print("Record deleted.")
    else:
        print("This name is not found.")
        
        
# "save_contacts" function preserves the specified object and saves it in the contacts file.
def save_contacts(mycontacts):
    # open the file for entry 
    output_file = open(FILENAME, "wb")
    
    # pickle the dictionary and save it 
    pickle.dump(mycontacts, output_file)
    
    # close the file 
    output_file.close()
    
# call main function
main()

