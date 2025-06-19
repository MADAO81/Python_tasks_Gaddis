# This program demonstrates the range_sum function.

def main():
    # create list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Get the sum of the values in the index positions, starting from 2 up to 5.
    my_sum = range_sum(numbers, 2, 5)
    
    # show sum 
    print("The sum of values from 2 up to 5 is: ", my_sum)
    
# The range_sum function returns the sum of the specified
# range of values in the num list. The start parameter sets the index position of the initial value. 
# The end parameter sets the index position of the final value.
def range_sum(num_list, start, end):
    if start > end:
        return 0
    else: 
        return num_list[start] + range_sum(num_list, start + 1, end)
        
# call main function
main()