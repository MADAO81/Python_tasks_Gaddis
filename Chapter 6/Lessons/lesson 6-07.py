# This program demonstrates how numbers read from a file
# are converted from their string representation before
# they are used in a mathematical operation.

def main():
    infile = open('numbers.txt', 'r')

    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    infile.close()

    total = num1 + num2 + num3

    print("Numbers: ", num1, num2, num3)
    print("Sum of numbers: ", total)


main()
