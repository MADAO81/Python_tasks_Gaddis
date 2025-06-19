# Morse Code converter. Morse code is an encoding where each letter of the alphabet, 
# each digit, and various punctuation marks are represented by a series of dots and dashes.  
# Write a program that asks the user to enter a string value and then 
# converts this string value to Morse code encoding.

def main():
    # local valuables
    index = 0
    
    # list of Morse Code 
    morse_list = [' ', '--..--', '.-.-.-', '-----',
                  '.----', '..---', '...--', '....-',
                  '.....', '-....', '--...', '---..',
                  '----.', '.-', '-...', '-.-.', '-..',
                  '.', '..-.', '--.', '....', '..', '.---',
                  '-.-', '.-..', '--', '-.', '---', '.--.',
                  '--.-', '.-.', '...', '-', '..-', '...-',
                  '.--', '-..-', '-.-', '--..']
    
    # Get user's input
    morse_string = input("Enter the message to convert to Morse Code: ")
    
    # Sort through the characters in the string, determine the code index
    for ch in morse_string:
        # convert symbol to upper register
        ch = ch.upper()
        
        # determine index in list
        if ch == ' ':
            index = 0
        elif ch == ',':
            index = 1
        elif ch == '.':
            index = 2
        elif ch == '?':
            index = 3
        elif ch == '0':
            index = 4
        elif ch == '1':
            index = 5
        elif ch == '2':
            index = 6
        elif ch == '3':
            index = 7
        elif ch == '4':
            index = 8
        elif ch == '5':
            index = 9
        elif ch == '6':
            index = 10
        elif ch == '7':
            index = 11
        elif ch == '8':
            index = 12
        elif ch == '9':
            index = 13
        elif ch == 'A':
            index = 14
        elif ch == 'B':
            index = 15
        elif ch == 'C':
            index = 16
        elif ch == 'D':
            index = 17
        elif ch == 'E':
            index = 18
        elif ch == 'F':
            index = 19
        elif ch == 'G':
            index = 20
        elif ch == 'H':
            index = 21
        elif ch == 'I':
            index = 22
        elif ch == 'J':
            index = 23
        elif ch == 'K':
            index = 24
        elif ch == 'L':
            index = 25
        elif ch == 'M':
            index = 26
        elif ch == 'N':
            index = 27
        elif ch == 'O':
            index = 28
        elif ch == 'P':
            index = 29
        elif ch == 'Q':
            index = 30
        elif ch == 'R':
            index = 31
        elif ch == 'S':
            index = 32
        elif ch == 'T':
            index = 33
        elif ch == 'U':
            index = 34
        elif ch == 'V':
            index = 35
        elif ch == 'W':
            index = 36
        elif ch == 'X':
            index = 37
        elif ch == 'Y':
            index = 38
        elif ch == 'Z':
            index = 39
            
        # show Morse Code for this symbol
        print(morse_list[index], ",", sep = "", end = "")
        
# call main function
main()
        
    
    