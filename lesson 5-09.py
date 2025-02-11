# This program demonstrates a function that accepts 2 string arguments

def main():
    first_name = input("Enter your fist name: ")
    last_name = input("Enter your last name: ")
    print("Your full name in reverse: ")
    reverse_name(first_name, last_name )

def reverse_name(first, last):
    print(last,first)
    
# Call main function
main()