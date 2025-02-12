# This program shows a  five random numbers from 1 to 100
import random

def main():
    for count in range(5):
        print("Your number is: ",random.randint(1,100))

# Call main function    
main()
