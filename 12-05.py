# The recursive sum of the list.

def main():
    # initialize list of values from 1 to 10
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # show list 
    print("Numbers list: \n", number_list, sep = "")
    
    # call function sum_list and show sum of all numbers in list 
    print("Sum of all numbers in list: ", sum_list(number_list))
    
# The sum_list function accepts a list of numbers as arguments. 
# This function recursively calculates the sum of all the numbers in the list and returns the value
def sum_list(numlist):
    n = len(numlist)
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[n-1] + sum_list(numlist[0:n-1])
        
# call main function
main()