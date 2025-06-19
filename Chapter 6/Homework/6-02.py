# Displaying the top of a file. Write a program that prompts the user for a file name.
# The program should display only the first five lines of the file's contents.
# If the file has fewer than five lines, it should display the entire file's contents.

def main():
    # Get the name of the file
    your_file = input("Enter the name of the file: ")
    infile = open("your_file", "r")
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()

    line1 = line1.rstrip('\n')
    line2 = line1.rstrip('\n')
    line3 = line1.rstrip('\n')
    line4 = line1.rstrip('\n')
    line5 = line1.rstrip('\n')

    # Close the file
    infile.close()

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)


main()
