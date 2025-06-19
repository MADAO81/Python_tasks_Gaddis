# the sum of the numbers

def main():
    # local valuable
    num = 0
    
    # get the number from user 
    while num <= 0:
        num = int(input("Enter the positive integer: "))
    
    # call sum_num function and show the sum 
    print("The sum from 1 to ", num, "is", format(sum_nums(num), ","))
    
# The sum_nung function takes an integer argument and returns the sum of all integers starting from 1 to the number passed as an argument.
def sum_nums(n):
    if n == 0:
        return n 
    else:
        return n + sum_nums(n-1)
        
# call main function
main()