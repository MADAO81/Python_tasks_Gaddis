# This program use function for calculate sum of values in the list

def main():
    # create list
    numbers = [2, 4, 6, 8, 10]
    
    # show sum of elements in list
    print("Sum of elements in list: ", get_total(numbers))
    
# Function get_total accepts list as argument 
# and returns sum of values in list
def get_total(value_list):
    # create variable  to use as storage
    total = 0 
    
    # calculate sum of elements in list 
    for num in value_list: 
        total += num
        
    # return sum 
    return total
    
# call main function
main()