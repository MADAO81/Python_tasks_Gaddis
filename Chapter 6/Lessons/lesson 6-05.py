# This program reads the contents of the file philosophers.txt line by line.

def main():
    # Open the file philosophers.txt
    infile = open("philosophers.txt", "r")
    
    # Read 3 strings from the file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    # Delete \n from each sring line 
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    # Close the file
    infile.close()
    
    # Print received values
    print(line1)
    print(line2)
    print(line3)
    
# Call main method
main()