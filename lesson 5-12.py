# This program demonstrates passing two string values as named arguments to a function.

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print("Your full name in reverse: ")
    reverse_name(last=last_name, first = first_name)
    
def reverse_name(first, last):
    print(last, first)
    
# Call main function.
main()