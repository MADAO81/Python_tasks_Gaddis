# Recursive multiplication

def main():
    # local valuables 
    num1 = 0
    num2 = 0
    
    # Get the first positive non-negative integer from the user.
    while num1 <= 0:
        num1 = int(input("Enter the first number: "))
        
    # Get the second positive non-negative integer from the user.
    while num2 <= 0:
        num2 = int(input("Enter the second number: "))
        
    # call multiply function and show result 
    print(num1, "multiply by", num2, "is", multiply(num1, num2))
    
# The multiply function is a recursive function that takes two arguments to the parameters x and y, 
# and returns the value of x multiplied by y. This function assumes that x and y always contain positive non-negative integers.
def multiply(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + multiply(x, y - 1)
            
# call main function
main()