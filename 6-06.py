# Arithmetic mean. There is a file numbers_6_5.txt
# Write a program that read all values and calculate the arithmetic mean

def main():
    # create counter of numbers
    total = 0
    
    # create counter of quantity 
    quantity_counter = 0
    
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
        quantity_counter += 1 
        
        # read the next line
        line = work_file.readline()
        
    # close the file
    work_file.close()
    
    # calculate arithmetic mean
    arithmetic_mean = total/quantity_counter
    
    # show result
    print("Arithmetic mean of numbers in the file : ", arithmetic_mean)
    
    
# Call main function
main()