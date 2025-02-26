# This program reads and displays the contents of the file philosophers.txt 
def main():
    # Open file witn name philosophers.txt
    infile = open('philosophers.txt', 'r')
    
    # Read the contents of file
    file_contents = infile.read()
    
    # Close the file 
    infile.close()
    
    # Print the data read into RAM
    print(file_contents)
    
# Call the main function
main()