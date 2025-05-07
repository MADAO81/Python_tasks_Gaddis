# BankAccount class simulates bank account

class BankAccount:

    # __init__ method gets argument with balance on account
    # it is assigned to the attribute __balance

    def __init__(self, bal):
        self.__balance = bal

    # "deposit" method adds money to account
    def deposit(self, amount):
        self.__balance += amount

    # "withdraw" method withdraws the amount from the account
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Error: insufficient founds.")

    # get_balance method returns balance of funds in the account.

    def get_balance(self):
        return  self.__balance

    # __str__ method returns string value reporting the state of an object.
    def __str__(self):
        return "The remainder is $" + format(self.__balance, ".2f")
