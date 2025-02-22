# Feet in inches.
# One foot equals 12 inches. Write a feet to inches function
# that takes the number of feet as an argument and returns the number
# of inches in that number of feet. Apply this function in a program that prompts 
# the user to enter the number of feet and then shows the number
# of inches in that number of feet.
INCHES_IN_FOOT = 12


def main():
    feet = float(input("Enter the number of feet that you want to convert: "))
    print(f"In {feet} feet - {feet_to_inches(feet):.2f} inches.")


def feet_to_inches(feet):
    inches = feet * INCHES_IN_FOOT
    return inches


main()
