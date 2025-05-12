# This program transmits the Coin object as an argument to the function.
import coin 

# main function
def main():
    # create a Coin object
    my_coin = coin.Coin()
    
    # this instruction will show "Heads"
    print(my_coin.get_sideup())
    
    # Pass the object to the flip function.
    flip(my_coin)
    
    # this instruction can "Heads" or "Tails"
    print(my_coin.get_sideup())
    
# flip function toss the coin 
def flip(coin_obj):
    coin_obj.toss()
    
# call main function
main()

    