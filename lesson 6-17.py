# This program allows the user to search the coffee.txt file
# for entries that match the description

def main():
    # Create a boolean variable to use as a flag.
    found = False

    # Get the desired value.
    search = input("Enter the description you are looking for: ")

    # Open file coffee.txt
    coffee_file = open("coffee.txt", "r")

    # Read the field with description of coffee first record
    descr = coffee_file.readline()

    # Read the rest of file
    while descr != "":
        # Read the field with quantity
        qty = float(coffee_file.readline())

        # Delete \n from description
        descr = descr.rstrip("\n")

        # Determine if this entry matches the value you are looking for
        if descr == search:
            # Show record
            print("Description: ", descr)
            print("Quantity: ", qty)
            print()
            # Set the found flag to True.
            found = True

        # Read the next description
        descr = coffee_file.readline()

    # Close file
    coffee_file.close()

    # If the search value is not found in the file, then show a message.
    if not found:
        print("This value was not found in the file.")

# Call main function
main()
