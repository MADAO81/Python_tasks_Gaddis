# Alphabetic Phone Number Translator

def main():
    # local valuables
    digit_list = ["2", "3", "4", "5", "6", "7", "8", "9"]
    alpha_phone_number = " "
    num_phone_number = " "
    
    # Get user's input
    alpha_phone_number = input("Enter the phone number in format XXX-XXX-XXXX")
    
    # Iterate through the characters of the string value, 
    # searching for the index number for each character in the list of digits. 
    # Construct a string value and show the numbers.
    for ch in alpha_phone_number:
        # Determine if a character is a letter.
        if ch.isalpha():
            # If yes, than convert it to upper register
            ch = ch.upper()
            # Determine index number for symbol from numbers list 
            if ch == "A" or ch == "B" or ch == "C":
                index = 0
            elif ch == 'D' or ch == 'E' or ch == 'F':
                index = 1
            elif ch == 'G' or ch == 'H' or ch == 'I':
                index = 2
            elif ch == 'J' or ch == 'K' or ch == 'L':
                index = 3
            elif ch == 'M' or ch == 'N' or ch == 'O':
                index = 4
            elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
                index = 5
            elif ch == 'T' or ch == 'U' or ch == 'V':
                index = 6
            elif ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z':
                index = 7
            # Assign a number from the list to the symbol.
            ch = digit_list[index]
            
        # concatenate numbers to string 
        num_phone_number = num_phone_number + ch 
        
    # show digits for phone number
    print("Phone number: ", num_phone_number)

# call main function
main()
                