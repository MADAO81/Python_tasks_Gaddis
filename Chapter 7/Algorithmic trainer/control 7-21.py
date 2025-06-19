# constants to rows and colons
def main():
    # create two-dimensional list
    values = [[ 1, 2], 
              [ 10, 20],  
              [ 100, 200],
              [ 1000, 2000]]
    
    # Fill list with random numbers
    for r in range(4):
        for c in range(2):
            print(values [r][c])

    
# call main function
main()