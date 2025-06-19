# This program creates an instance of the SavingsAccount class and an instance of the CD class.

import accounts 

def main(): 
    # Get the account number, the interest rate, and the balance of the savings account
    print("Enter your savings account information.")
    acct_num = input("Account number: ")
    int_rate = float(input("The interest rate: "))
    balance = float(input("Remains: "))
    
    # Create SavingsAccount object
    savings = accounts.SavingsAccount(acct_num, int_rate, balance)
    
    # Get the account number, the interest rate, the account balance, and the maturity date of the CD account.
    print("Enter information about account CD: ")
    acct_num = input("Account number: ")
    int_rate = float(input("The interest rate: "))
    balance = float(input("Remains: "))
    maturity = input("Repayment date: ")
    
    # Create CD object
    cd = accounts.CD(acct_num, int_rate, balance, maturity)
    
    # Show the entered data.
    print("Here is the data you entered: ")
    print()
    print("Savings account")
    print("================")
    print("Account number: ", savings.get_account_num())
    print("Interest rate: ", savings.get_interest_rate())
    print("Remains: $", format(savings.get_balance(), ".2f"), sep = "")
    print()
    print("Account of the deposit certificate (CD)")
    print("=======================================")
    print("Account number: ", cd.get_account_num())
    print("Interest rate: ", cd.get_interest_rate())
    print("Remains: $", format(cd.get_balance(), ".2f"), sep = "")
    print("Repayment date: ", cd.get_maturity_date())
    
# call main function
main()
