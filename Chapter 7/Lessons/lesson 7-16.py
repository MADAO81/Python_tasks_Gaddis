# this program saves list of numbers to file 

def main(): 
    # create numbers list
    numbers = [1, 2, 3, 4, 5, 6, 7]

    # open file to write
    outfile = open("numberlist.txt", "w")
    
    # write list to file 
    for item in numbers: 
        outfile.write(str(item) + "\n")
        
    # close file 
    outfile.close()
    
# call main function
main()