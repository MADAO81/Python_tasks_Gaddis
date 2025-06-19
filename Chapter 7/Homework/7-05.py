# checking the validity of the expense account number.  the file charge_accounts.txt 
# contains a list of acceptable numbers of the company's expense accounts. 
# Each account number is a seven-digit number, in particular 5658845. 
# Write a program that reads the contents of a file into a list. 
# This program should then ask the user to enter the expense account number. 
# The program must determine that the number is valid by searching for it in the list. If 
# if there is a number in the list, the program should display a message indicating that the number is valid. 
# If the number is not in the list, the program should output a message indicating that the number is invalid.

def main():
    # open file
    file_open = open("charge_accounts.txt ", "r")
    
    # read lines to list
    accounts = file.readlines()
    
    # Cut "\n" from elements of list
    for i in range (len(accounts)):
        accounts[i] = accounts[i].rstrip("\n")
        
    # Get account number from user
    user_account = int(input("Enter your account number: "))
    
    if user_account in accounts:
        print("Account number", user_account,"is valid.")
    else:
        print("Account number", user_account,"is invalid.")
        
# call main function
main()