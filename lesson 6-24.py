# This program shows contents of a file

def main():
    # Get the name of a file
    filename = input("Enter file name: ")

    # Open file
    infile = open(filename, "r")

    # Read contents of a file
    contents = infile.read()

    # Show contents of file
    print(contents)

    # Close the file
    infile.close()

# Call main function
main()