import random

# "Coin" class imitates coin, that you need to toss up

class Coin: 
    # __init__ method initializes data attribute sideup with value "Heads"
    
    def __init__(self):
        self.sideup = "Heads"
        
    # The toss method generates a random number
    # in the range from  0 to 1. if this number
    # is 0, then the sideup gets the value 'Heads'. 
    # Otherwise, slideup gets the value 'Tails'.
    
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"
    
    # The get_sideup method returns the value  referenced by slideup.
    
    def get_sideup(self):
        return self.sideup
        
# main function
def main():
    # Create an object based on a class "Coin"
    my_coin = Coin()
    
    # Show the up-facing side of the coin.
    print("This side is facing up: ", my_coin.get_sideup())
    
    # Toss the coin 
    print("I 'm tossing up a coin ...")
    my_coin.toss()
    
    # But now I'm lying! In this object
    # I'm going to directly change
    # the value of the side up attribute to 'Heads'.
    my_coin.sideup = "Heads"
    
    # Show the up-facing side of the coin.
    print("This side is facing up: ", my_coin.get_sideup())
    
# call main function
main()
