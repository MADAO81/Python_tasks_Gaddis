# This program allows the user to change the quantity in the coffee.txt file entry.
import os


def main():
    # Create boolean value to use it as a flag
    found = False

    # Get the desired value and the new quantity.
    search = input("Enter the desired description: ")
    new_qty = int(input("Enter the new quantity: "))

    # Open source file coffee.txt
    coffee_file = open("coffee.txt", "r")

    # Open temporary file
    temp_file = open("temp.txt", "w")

    # Read the field with description of first record.
    descr = coffee_file.readline()

    # Read the rest of file
    while descr != "":
        # Read the field with quantity
        qty = float(coffee_file.readline())

        # Delete \n from description
        descr = descr.rstrip("\n")

        # Write to temporary file this record or new record if this record needed to change
        if descr == search:
            # Write to temporary file changed record
            temp_file.write(descr + "\n")
            temp_file.write(str(new_qty) + "\n")

            # Set the found flag to True.
            found = True
        else:
            # Write the original record to a temporary file
            temp_file.write(descr + "\n")
            temp_file.write(str(new_qty) + "\n")

        # Read the next description
        descr = coffee_file.readline()

    # Close file with coffee data and temporary file
    coffee_file.close()
    temp_file.close()

    # Delete original file
    os.remove("coffee.txt")

    # Rename temp file
    os.rename("temp.txt", "coffee.txt")

    # If the search value is not found in the file, then show a message.
    if found:
        print("File updated.")
    else:
        print("This value is not found in file.")

# Call main function
main()