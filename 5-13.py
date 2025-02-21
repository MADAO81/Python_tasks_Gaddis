# The maximum of two values.
# Write a function called "max" that takes two integer values
# as arguments and returns the value that is larger of the two.
# For example, if 7 and 12 are passed as arguments, the function should return 12.
# Use the function in a program that prompts the user to enter two integer values.
# The program should display the larger of the two.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def max(a,b):
    if a >b:
        return a
    elif a < b:
        return b
    else:
        return print("Your numbers are equal!")

bigger_number = max(a,b)
print("The bigger number is: ", bigger_number)
