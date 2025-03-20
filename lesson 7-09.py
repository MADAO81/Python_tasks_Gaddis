# This program calculates arithmetic mean

def main():
    # create list
    numbers = [2.5,4.6,6.13,8.63,10.96]
    
    # create variable to use as storage
    total = 0 
    
    # calculate sum of values in list
    for value in numbers: 
        total += value
        
    # calculate arithmetic mean
    average = total/ len(numbers)
        
    # show sum of values
    print("Arithmetic mean in list : ", total)
    
# call main function
main()