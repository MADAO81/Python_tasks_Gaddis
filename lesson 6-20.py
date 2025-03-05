# This program divides one number by another

def main():
    # Get two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Divide num1 by num2 and show result
    result = num1 / num2
    print(f"{num1} divided by {num2} is {result:.2f}")

# Call main function
main()