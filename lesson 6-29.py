# This program shows the total sales amount in file sales_data.txt

def main():
    # Initialize storage
    total = 0.0

    try:
        # Open file
        infile = open('sales_data.txt', 'r')

        # Read the values from file and save them to the storage
        for line in infile:
            amount = float(line)
            total += amount

        # Close the file
        infile.close()

        # Print total amount
        print(f"{total:.2f}")

    except Exception as err:
        print(err)

# Call main function
main()