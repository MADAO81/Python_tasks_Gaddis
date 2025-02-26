# This program writes three lines of data to the file.
def main():
    # Open file philosophers.txt.
    outfile = open('philosophers.txt', 'w')
    
    # Write names of 3 philosophers to the file 
    outfile.write("John Lokk\n")
    outfile.write("David Hume\n")
    outfile.write("Edmund Burke\n")
    
    # Close the file 
    outfile.close()
    
# Call the main function
main()