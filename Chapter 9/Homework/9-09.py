# Black Jack

# Global constant for win 
MAX = 21

# main function 
def main():
    # local valuables 
    hand1 = 0
    hand2 = 0
    deck = create_deck()
    
    while hand1 <= MAX and hand2 <= MAX:
        
        # Distribute the cards to each player and calculate 
                 # the value of the combination of cards in their hands
        card1, value1 = deck.popitem()
        hand1 = update_hand_value(hand1, value1, card1)
        
        card2, value2 = deck.popitem()
        hand2 = update_hand_value(hand2, value2, card2)
        
        print("Player 1 get card: ", card1)
        print("Player 2 get card: ", card2)
        print()
        
    # Determine the winner 
    if hand1 > MAX and hand2 > MAX:
        print("There is no winner!")
    elif hand1 > 21:
        print("Player 2 wins.")
    else:
        print("Player 1 wins.")
        
# create_deck function creates deck of cards and returns the deck 
def create_deck():
    # create local valuables 
    suits = ["spades", "hearts", "clubs", "diamonds"]
    special_values = {"ace":1, "king":10, "queen":10, "jack":10}
    
    # create the list of all cards  values
    numbers = ["ace", "king", "queen", "jack"]
    for i in range(2,11):
        numbers.append(str(i))
        
    # initialize the deck 
    deck = {}
    for suit in suits: 
        for num in numbers: 
            # values 2-10
            if num.isnumeric():
                deck[num + " " + suit] = int(num)
            # Ace, king, queen or jack
            else:
                deck[num + " " + suit] = special_values[num]
    return deck
    
def update_hand_value(hand, value, card):
    if not card.startswith("Ace"):
        return hand+value 
    # Adding 11 calls exceeding the maximum
    elif hand > 10:
        # The default value is 1 
        return hand + value 
    else: 
        return hand + 11 
        
# call main function
main()