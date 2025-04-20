# This program used dictionary to create card deck
import random

def main():
    # Create card deck
    deck = create_deck()

    # Get number of card for dealing
    num_cards = int(input("How many cards to deal? "))

    # Dealing cards
    deal_cards(deck, num_cards)


# Create_deck function returns dictionary as card deck
def create_deck():
    # Create dictionary thant contains cards as key/value
    deck = {"Ace of Spades": 1, "2 of Spades": 2, "3 of Spades": 3,
            "4 of Spades": 4, "5 of Spades": 5, "6 of Spades": 6,
            "7 of Spades": 7, "8 of Spades": 8, "9 of Spades": 9,
            "10 of Spades": 10, "Jack of Spades": 10, "Queen of Spades": 10,
            "King of Spades": 10,

            "Ace of Hearts": 1, "2 of Hearts": 2, "3 of Hearts": 3,
            "4 of Hearts": 4, "5 of Hearts": 5, "6 of Hearts": 6,
            "7 of Hearts": 7, "8 of Hearts": 8, "9 of Hearts": 9,
            "10 of Hearts": 10, "Jack of Hearts": 10, "Queen of Hearts": 10,
            "King of Hearts": 10,

            "Ace of Clubs": 1, "2 of Clubs": 2, "3 of Clubs": 3,
            "4 of Clubs": 4, "5 of Clubs": 5, "6 of Clubs": 6,
            "7 of Clubs": 7, "8 of Clubs": 8, "9 of Clubs": 9,
            "10 of Clubs": 10, "Jack of Clubs": 10, "Queen of Clubs": 10,
            "King of Clubs": 10,

            "Ace of Diamonds": 1, "2 of Diamonds": 2, "3 of Diamonds": 3,
            "4 of Diamonds": 4, "5 of Diamonds": 5, "6 of Diamonds": 6,
            "7 of Diamonds": 7, "8 of Diamonds": 8, "9 of Diamonds": 9,
            "10 of Diamonds": 10, "Jack of Diamonds": 10, "Queen of Diamonds": 10,
            "King of Diamonds": 10
            }

    # return deck
    return deck


# The deal cards function deals a specified number of cards
# FROM THE DECK.

def deal_cards(deck, number):
    # Initialize storage for number of cards in hands
    hand_value = 0

    # Make sure that the number of cards to be dealt is not greater than
    # the number of cards in the deck.
    if number > len(deck):
        number = len(deck)

    # Deal cards and calculate its values
    for count in range(number):
        card, value = deck.popitem()
        print(card)
        hand_value += value

    # Show the value of cards in your hand.
    print("Value of cards in your hand: ", hand_value)


# call main function
main()
