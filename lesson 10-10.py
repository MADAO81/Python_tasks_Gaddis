# This program demonstrates the BankAccount class with added __str__ method

import bankaccount2
def main():
    # Get the initial balance.
    start_bal = float(input("Enter your initial balance: "))

    # create an object "BankAccount"
    savings = bankaccount2.BankAccount(start_bal)

    # add salary to user's account
    pay = float(input("How much did you earn this week?"))
    print("Add this sum to your deposit.")
    savings.deposit(pay)

    # Show balance
    print(savings)

    # Get an amount to withdraw from a bank account.
    cash = float(input("What amount would you like to withdraw from your account?"))
    print("Withdraw this sum from your account.")
    savings.withdraw(cash)

    # Show balance
    print(savings)

    # call main function


main()
