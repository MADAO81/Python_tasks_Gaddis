# This program imports the coin module and creates an instance of the Coin class.

import coin

def main():
    # Create an object based on a class "Coin"
    my_coin = coin.Coin()
    
    # Show the up-facing side of the coin.
    print("This side is facing up: ", my_coin.get_sideup())
    
    # Toss the coin 
    print("I 'm tossing up a coin 10 times:")
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())
    
# call main function
main()
