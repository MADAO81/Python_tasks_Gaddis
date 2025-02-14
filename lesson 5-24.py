# This program demonstrates the function 'sqrt'

import math

def main():
    # Get number
    number = float(input("Enter the number: "))
    
    # Get square root of the number
    square_root = math.sqrt(number)
    
    # Show square root 
    print("Square root of", number, "is: ", square_root)
    
main()