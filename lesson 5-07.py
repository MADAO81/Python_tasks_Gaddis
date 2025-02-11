#This program converts the number of cups to FL oz
def main():
    # Show start screen.
    intro()
    # Get the number of cups
    cups_needed = int(input("Enter the number of cups: "))
    # Convert number of cups to fl oz
    cups_to_ounces(cups_needed)
    
# Function 'intro' shows start screen
def intro():
    print("This program converts")
    print("cups to fl oz.")
    print("For information here is the converting formula: ")
    print("1 cup = 8 fl oz")
    print()
    
# Function 'cups_to_ounces' accepts the number of cups 
# and shows an equivalent amount of fl oz
def cups_to_ounces(cups):
    ounces = cups * 8 
    print("It converting to", ounces,"ounces.")
    
# Call the main function 
main()
    