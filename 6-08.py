# a program for read a file with random numbers(1-500), show sum of numbers and quantity of numbers
def main():
    # create counter four numbers quantity
    numbers_quantity = 0
    
    # create counter for sum of numbers
    numbers_sum = 0 
    
    # open file with numbers
    work_file = open("random_numbers.txt", "r")
    
    # Read the first line from file
    # but not  convert it to a number yet.
    # First, you need to check for an empty string value.
    line = work_file.readline()
    
    # continue processing until an empty line is returned from readline
    while line !="":
        #convert string to floating point number 
        digit = float(line)
        
        # add unit to numbers_quantity storage 
        numbers_quantity += 1 
        
        # add number to sum of numbers
        numbers_sum += digit
        
        # read the next line
        line = work_file.readline()
        
    # close the file
    work_file.close()
    
    # Show results
    print(f"Sum of numbers in your file: {numbers_sum}")
    print(f"Quantity of numbers in your file: {numbers_quantity}")
    
# Call main function
main()
    