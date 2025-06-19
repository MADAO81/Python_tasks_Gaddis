# this program  save list of string values to file 

def main():
    # Create list of string values
    cities = ["New-York", "London", "Moscow", "Tokyo", "Beijing"]
    
    # Open file to write 
    outfile = open("cities.txt","w")
    
    # Write list to file 
    for item in cities: 
        outfile.write(item + "\n")
    
    # close file
    outfile.close()
    

# call main function
main()
