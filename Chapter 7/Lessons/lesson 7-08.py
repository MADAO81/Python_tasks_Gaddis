# This program calculates sum of values in list

def main():
    # create list
    numbers = [2,4,6,8,10]
    
    # create variable to use as storage
    total = 0 
    
    # calculate sum of values in list
    for value in numbers: 
        total += value
        
    # show sum of values
    print("Sum of elements: ", total)
    
# call main function
main()