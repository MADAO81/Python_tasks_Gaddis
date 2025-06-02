# The recursive exponentiation method

# Global constants for minimum and maximum exponents
MIN = 1 
MAX = 100 

def main():
    # local valuables 
    num = 0.0 
    exp = 0 
    
    # get a number from the user
    num = float(input("Enter a number: "))
    
    # Get a degree indicator from a user
    while exp < MIN or exp > MAX:
        exp = int(input("Enter a positive integer between " + str(MIN) + " and " + str(MAX) + ": "))
        
    # Call the power function and show the result.
    print(num, "raised to a power", exp, "is", format(power(num, exp), ",.2f"))
    
# The power function uses recursion to exponentiate a number.
# This function takes two arguments: a number to be raised to a power, and an exponent.
# This function assumes that the exponent is a non-negative integer.
def power(x, y):
    if y == 0:
        return 1 
    else:
        return x * power(x, y - 1)
        
# call main function
main()