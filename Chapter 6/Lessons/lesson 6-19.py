# This program allows the user to delete a record from a file.
import os # this module needed for 'remove' and 'rename' functions

def main():
    # Create boolean value to use it as a flag
    found = False

    # Get coffee brand, which need to delete
    search = input("Which brand do you need to delete? ")

    # Open original file coffee.txt
    coffee_file = open("coffee.txt", "r")

    # Open temporary file
    temp_file = open("temp.txt", "w")

    # Read the field with description of the first record
    descr = coffee_file.readline()

    # Read the rest of the file
    while descr !="":
        # Read the field with quantity
        qty = float(coffee_file.readline())

        # Delete \n from description
        descr = descr.rstrip("\n")

        # If this record is not intented to deletion, record it to the temp file
        if descr != search:
            # Write original record to the temporary file
            temp_file.write(descr + "\n")
            temp_file.write(str(qty) + "\n")
        else:
            # Set the 'found' flag to True.
            found = True

        # Read the next description
        descr = coffee_file.readline()

    # Close the file with data and temporary file
    coffee_file.close()
    temp_file.close()

    # Delete original file
    os.remove("coffee.txt")

    # Rename temp file
    os.rename("temp.txt", "coffee.txt")

    # If the value you are looking for is not found in the file, show message
    if found:
        print("File updated.")
    else:
        print("This value not found in file.")

# Call main function
main()





