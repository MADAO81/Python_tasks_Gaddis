# The SavingsAccount class represents a savings account.

class SavingsAccount:
    
    # The init method accepts arguments for the account number, interest rate, and balance.
    
    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__interest_rate = int_rate
        self.__balance = bal

    # The following methods are data attribute modifier methods.
    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    def set_balance(self, bal):
        self.__balance = bal
        
    # The following methods are methods that receive data attributes.
    
    def get_account_num(self):
        return self.__account_num

    def get_interest_rate(self):
        return self.__interest_rate

    def get_balance(self):
        return self.__balance
        
# The CD class represents the account
# of the Certificate of Deposit (CD). 
# This is a subclass of the SavingsAccount class.

class CD(SavingsAccount):
    
    # The init method accepts arguments for the account number, interest rate, balance, and maturity date.

    def __init__(self, account_num, int_rate, bal, mat_date):
        # Call __init__ method of superclass
        SavingsAccount.__init__(self, account_num, int_rate, bal)
        
        # initialize attribute __maturity_date 
        self.__maturity_date = mat_date
        
    # The set_maturity_date method is a modifier method for the _maturity_date attribute.
    
    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date
        
    # The get_maturity_date method is the recipient method of the _maturity_date attribute.
    def get_maturity_date(self):
        return self.__maturity_date
        
        