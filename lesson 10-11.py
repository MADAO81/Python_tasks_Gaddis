# This program imports a simulation module and creates three instances of the Coin class.

import coin 

def main():
    # create 3 objects of Coin class 
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()
    
    # Show the upturned side of each coin.
    print("Here are three coins with these sides facing up:")
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()
    
    # Toss the coin 
    print("I flip up all three coins ...")
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()
    
     Show the upturned side of each coin.
    print("Now these sides are facing up::")
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()
    
# Call main function
main()
