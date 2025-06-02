# recursive strings 

def main():
    # local valuable 
    number = 0
    
    # Get the number of rows from the user.
    number = int(input("How many lines to show?"))
    
    # Show lines 
    print_lines(number)
    
# The print_lines function is a recursive function that takes an integer argument, n. The function shows n lines of asterisks on the screen, 
# with the first line showing 1 asterisk, the second line showing 2 asterisks, up to the nth with n asterisks.
    
def print_lines(n):
    if n > 1:
        print_lines(n-1)
    for i in range(n):
        print("*", end = "")
    print()
    
# call main function
main()