# This program shows a  five random numbers from 1 to 100
import random

def main():
    for count in range(5):
        # Get a random numbers
        number = random.randint(1,100)
        # Show a random number
        print("Your number is: ", number)

# Call main function    
main()
