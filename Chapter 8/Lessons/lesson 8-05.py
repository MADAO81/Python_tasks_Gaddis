#This program demonstrates several string validation methods.

def main():
    # Get string value from user
    user_string = input("Enter the string value: ")
    
    print("Here is what is found regarding the entered value: ")
    
    # analise string value
    if user_string.isalnum():
        print("This string contains letters or numbers.")
    if user_string.isdigit():
        print("This string contains only numerals.")
    if user_string.isalpha():
        print("This string contains only the alphabet letters.")
    if user_string.isspace():
        print("This string contains only the whitespace chars.")
    if user_string.islower():
        print("All letters in this string are in the lower register.")
    if user_string.isupper():
        print("All letters in this string are in the upper register.")
        
# call main function
main()