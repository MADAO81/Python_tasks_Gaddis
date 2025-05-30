# This program uses recursion to calculate the factorial of a number.

def main():
    # Get an integer from user 
    number = int(input("Enter a non-negative integer: "))
    
    # Get a factorial of integer
    fact = factorial(number)
    
    # Show factorial of integer
    print("Factorial of integer", number, " is", fact)
    
    # The factorial function uses recursion to calculate the factorial of its argument, which is assumed to be non-negative.
def factorial(num):
    if num == 0:
        return 1 
    else:
        return num * factorial(num - 1)

# call main function
main()
