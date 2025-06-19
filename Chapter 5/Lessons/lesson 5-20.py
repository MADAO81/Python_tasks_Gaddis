# This program simulates 10 coin tosses.
import random

# Constants
HEADS = 1 # Averse
TAILS = 2 # Reverse 
TOSSES = 10 # Quantity of tosses 

def main():
    for toss in range(TOSSES):
        # Simulate coin toss 
        if random.randint(HEADS,TAILS) == HEADS:
            print("Averse!")
        else:
            print("Reverse!")
            
# call main function
main()