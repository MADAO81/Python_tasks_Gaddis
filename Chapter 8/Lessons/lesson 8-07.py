# This program receives a password from the user and checks its validity

import login2

def main():
    # get password from user 
    password = input("Enter your password: ")
    
    # Check the valdity of the password
    while not login2.valid_password(password):
        print("This password is incorrect.")
        password = input("Enter your password: ")
    
    print("This is the correct password.")
    
# call main function
main()