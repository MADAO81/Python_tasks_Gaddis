# This program reads all values from sales.txt

def main():
    sales_file = open("sales.txt", "r")

    # Read the first line from file
    # but not  convert it to a number yet.
    # First, you need to check for an empty string value.
    line = sales_file.readline()
    # Continue processing until an empty line is returned from readline.
    while line != "":
        # Convert string to floating point number.
        amount = float(line)

        # Format and show the sum
        print(format(amount, ".2f"))

        # Read the next line
        line = sales_file.readline()

    # Close the file
    sales_file.close()


main()
