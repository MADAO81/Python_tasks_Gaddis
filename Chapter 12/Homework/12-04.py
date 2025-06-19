# The maximum value in the list.

def main():
    # initialize values list from 1 to 10
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # show list 
    print("Numbers list: \n", number_list, sep = "")
    
    # Call the find_largest function and show the maximum number in the list.
    print("Greatest number in list: ", find_largest(number_list))
    
# The find_largest function takes a list as an argument and returns the maximum value in the list. 
# This function uses recursion to find the maximum value.
def find_largest(numlist):
    n = len(numlist)
    if n == 1:
        return numlist[0]
    else:
        temp = find_largest(numlist[0:n-1])
        if numlist[n-1] > temp:
            return numlist[n-1]
        else:
            return temp
            
# call main function
main()