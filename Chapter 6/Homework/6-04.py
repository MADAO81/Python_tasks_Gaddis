# Values counter. There is a file names_6_4.txt with names.
# Write a program that shows quantity of names in file

def main():
    # create counter
    total = 1
    
    # Open file
    work_file = open("names_6_4.txt","r")
    
    # Read the first line from file
    # check for an empty string value.
    line = work_file.readline()
    
    # Continue processing until an empty line is returned from readline.
    while line != ""

        # read the next line
        line = work_file.readline()
        total +=1 
        
    # close file
    work_file.close()
    print("Total names in file: ",total)
    
    
# Call main function
main()