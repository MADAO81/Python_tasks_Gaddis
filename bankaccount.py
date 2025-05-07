# The BankAccount class simulates a bank account.

class BankAccount:
    # "__init__" method gets argument with the balance on the account
    # It is assigned to the attribute __balance

    def __init__(self, bal):
        self.__balance = bal
    # "deposit" method adds money to account

    def deposit(self,amount):
        self.__balance += amount


    # The withdraw method withdraws an amount from the account.
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Error: insufficient founds")


    # "get balance" method returns balance of funds in the account.
    def get_balance(self):
        return self.__balance
