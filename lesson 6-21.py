# This program divides one number by another

def main():
    # Get two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # If num2 is not equal zero,
    # Divide num1 by num2 and show result
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} divided by {num2} is {result:.2f}")
    else:
        print("Divide by zero is not allowed!")
# Call main function
main()