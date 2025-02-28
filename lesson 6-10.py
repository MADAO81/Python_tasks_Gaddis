# This program uses a 'for' cycle  to read file

def main():
    sales_file = open("sales.txt", "r")

    for line in sales_file:
        # Convert string to floating point number.
        amount = float(line)
        # Format and show the sum
        print(format(amount, ".2f"))

    # Close the file
    sales_file.close()

main()
