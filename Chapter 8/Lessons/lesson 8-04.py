# This program gets the user's first and last name, ID number.
# Based on this data, it generates a login name.

import login 

def main():
    # Get user's name, last name, ID number
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    idnumber = input("Enter your ID number: ")
    
    # Receive login to enter the system
    print("Your login to enter the system: ")
    print(login.get_login_name(first, last, idnumber))
    
# call main function
main()