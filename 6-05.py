# The sum of numbers. There is a file numbers_6_5.txt
# Write a program that read all values and calculate the sum of numbers in file

def main():
    # create counter
    total = 0
    
    # Open file
    work_file = open("numbers_6_5.txt","r")
    
    # Read the first line from file
    # but not  convert it to a number yet.
    # First, you need to check for an empty string value.
    line = work_file.readline()
    
    # continue processing until an empty line is returned from readline
    while line !="":
        # convert string to floating point number.
        amount = float(line)
        
        # add number to the counter
        total += amount
        
        # read the next line
        line = work_file.readline()
        
    # close the file
    work_file.close()
    
    # show total
    print("Sum of numbers in file: ",total)
    
    
# Call main function
main()