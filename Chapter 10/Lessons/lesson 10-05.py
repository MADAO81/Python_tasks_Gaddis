import random

# "Coin" class imitates coin, that you need to toss up

class Coin: 
    # __init__ method initializes data attribute __sideup with value "Heads"
    
    def __init__(self):
        self.__sideup = "Heads"
        
    # The toss method generates a random number
    # in the range from  0 to 1. if this number
    # is 0, then the __sideup gets the value 'Heads'. 
    # Otherwise, sideup gets the value 'Tails'.
    
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
    
    # The get_sideup method returns the value  referenced by slideup.
    
    def get_sideup(self):
        return self.__sideup
        

