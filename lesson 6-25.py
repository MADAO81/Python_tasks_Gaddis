# This program shows contents of a file

def main():
    # Get the name of a file
    filename = input("Enter file name: ")

    try:
        # Open file
        infile = open(filename, "r")

        # Read contents of a file
        contents = infile.read()

        # Show contents of file
        print(contents)

        # Close the file
        infile.close()
    except IOError:
        print("An error occurred while trying to read the file", filename)

# Call main function
main()