# recursive print 

def main():
    # local valuable 
    number = 0
    
    # Get a number from the user.
    number = int(input("How many numbers should I show?"))
    
    # show numbers 
    print_num(number)
    
# The print_num function is a recursive function that takes an integer argument, n, and prints
# numbers from 1 to n.
def print_num(n):
    if n > 1:
        print_num(n-1)
    print(n, sep = " ")
    
# call main function
main()