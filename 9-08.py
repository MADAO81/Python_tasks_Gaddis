# Names and email addresses

import pickle

# global constants for menu elements
LOOK_UP = 1 
ADD = 2 
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = r"data\emails.dat"

# Main function
def main():
    # get "emails" dictionary
    emails = load_email()
    
    # initialize valuable for user's choice 
    choice = 0 
    
    # Process user requests until the user completes the work.
    while choice != QUIT:
        choice = get_user_choice()
        
        if choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            add(emails)
        elif choice == CHANGE:
            change(emails)
        elif choice == DELETE:
            delete(emails)
            
    # Preserve the resulting dictionary
    save_emails(emails)
    
    print("Data saved.")
    
def load_emails():
    try:
        # Open file.
        input_file = open(FILENAME, "rb")
        
        # Deconserve the file 
        email_dict = pickle.load(input_file)
        
        # close file 
        input_file.close()
        
    # Couldn't open the dictionary.
    except IOError:
        # Create an empty dictionary
        email_dict = {}
        
    # return dictionary
    return email_dict
    
def get_user_choice():
    # Show menu, get user's choice and check it for validity
    print()
    print("Menu")
    print("=================================")
    print("1.Find email.")
    print("2.Add new name and email.")
    print("3.Change an existing email")
    print("4.Delete name and email.")
    print("5.Quit.")
    print()
    
    choice = int(input("Enter your choice: "))
    
    # Check chosen var 
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("The option you entered is incorrect. Please enter the correct option: "))
        
    # return chosen var 
    return choice 
    
def look_up(emails):
    # Get the name you are looking for.
    name = input("Enter the name: ")
    
    # Find the name in dictionary
    if name in emails:
        print("Name:", name)
        print("Email:", emails[name])
    else:
        print("Entered name is not found.")
        
def add(emails):
    # Get an email and name 
    name = input("Enter the name: ")
    address = input("Enter email: ")
    
    # Add a new address if the name does not exist.  Otherwise, notify the user that the name exists.
    if name not in emails: 
        emails[name] = address
        print("Name and email were added.")
    else: 
        print("This name already exists.")
        
def change(emails):
    # Get a name to update the information
    name = input("Enter the name: ")
    
    # Change email if name already exists. Otherwise, notify the user that the name is not exists.
    if name in emails:
        address = input("Enter the new address: ")
        emails[name] = address
        print("information updated.")
    else: # name not found 
        print("Name not found.")

def delete(emails):
    # Get a name to delete.
    name = input("Enter the name: ")
    
    if name in emails:
        
        del emails[name]
        print("Info deleted.")
        
    else: # name not found 
        print("Name not found.")
        
# The function preserves the specified dictionary and
# saves it in the emails file.
def save_emails(emails):
    # open file to record 
    output_file = open(FILENAME, "wb")
    
    # Conserve file and save 
    picle.dump(emails, output_file)
    
    # Close file 
    output_file.close()
    
# call main function
main()
    