# This program uses the return value of the function.

def main():
    # Get user's age 
    first_age = int(input("Enter your age: "))
    
    # Get user's best friend age 
    second_age = int(input("Enter your best friend's age: "))
    
    # Get sum of both ages 
    total = sum(first_age,second_age)
    
    # Show common age 
    print("Together you are", total, "years old.")

# The sum function takes two numeric arguments and returns the sum of these arguments.
def sum(num1,num2):
    # result = num1 + num2
    # return result
    return num1 + num2
    
# Call main function
main()