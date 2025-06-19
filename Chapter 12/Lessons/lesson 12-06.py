# This program uses recursion to find the greatest common divisor of two numbers.(GCD)

def main():
    # Get two numbers 
    num1 = int(input("Enter the integer: "))
    num2 = int(input("Enter another integer: "))
    
    # Show GCD 
    print("The greatest common divisor: ", gcd(num1, num2))
    
# GCD function returns greatest common divisor of two numbers 
def gcd(x,y):
    if x % y == 0:
        return y 
    else:
        return gcd(x, x % y)
        
# call main function
main()