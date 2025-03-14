# Line numbers. Write a program that prompts the user for a file name.
# Program should print file content. Every line should be with number and colons.

def main():
    # Get file name from user
    search_file = input("Enter the file name: ")
    
    # Open file
    infile = open("search_file", "r")
    
    # Read the first line from file
    # check for an empty string value.
    line = infile.readline()
    number_line = 1
    # Continue processing until an empty line is returned from readline.
    while line != ""
        # format and show line
        print(f"#{number_line}:{line}")
        
        # get the next line number 
        number_line +=1
        
        # read the next line
        line = infile.readline()
        
    # close file
    infile.close()
    
    
# Call main function
main()