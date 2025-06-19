# This program shows total amount of sales from file

def main():
    # initialize storage
    total = 0

    try:
        # Open file sales_data.txt
        infile = open('sales_data.txt', 'r')

        # Read values from file and save them to storage
        for line in infile:
            amount = float(line)
            total += amount

        # Close the file
        infile.close()

        # Print total sum
        print(f"{total:.2f}")
    except:
        print("Error!")

# Call main function
main()