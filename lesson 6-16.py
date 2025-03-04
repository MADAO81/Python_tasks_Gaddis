# This program shows records from file coffee.txt

def main():
    # Open file
    coffee_file = open("coffee.txt", "r")
    # Read the field with description of first record
    descr = coffee_file.readline()

    # Read the last of file
    while descr != "":
        # Read the field with the quantity
        qty = float(coffee_file.readline())

        # Delete \n from description
        descr = descr.rstrip("\n")

        # Show record
        print("Description: ", descr)
        print("Quantity: ", qty)

        # Read the next description
        descr = coffee_file.readline()

    # Close file
    coffee_file.close()


# Call main function
main()
