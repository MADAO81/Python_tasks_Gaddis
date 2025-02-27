# This program reads the contents of the file line by line philosophers.txt
def main():
    # Open the file
    infile = open('philosophers.txt', 'r')
    
    # Read 3 strings
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    # Close the file 
    
    # Print data
    print(line1)
    print(line2)
    print(line3)
    
# Call main function
main()