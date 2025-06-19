# This program "rolls" dice
import random

# Constants for minimum and maximum random numbers
MIN = 1
MAX = 6

def main():
    #Create a variable that controls the cycle.
    again = 'y'
    while again == 'y' or again == "Y":
        print("Throwing dice...")
        print("The numbers on the dice: ")
        print(random.randint(MIN,MAX))
        print(random.randint(MIN,MAX))
        
        # Make another roll of the dice
        again = input("Make another roll of the dice? (y = yes) : ")
        
main()