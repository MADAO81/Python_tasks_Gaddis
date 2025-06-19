# constants to rows and colons
ROWS = 3
COLS = 4

def main():
    # create two-dimensional list
    values = [[ 0, 0, 0, 0], 
              [ 0, 0, 0, 0],  
              [ 0, 0, 0, 0]]
    
    # Fill list with random numbers
    for r in range(ROWS):
        for c in range(COLS):
            values [r][c] = (0, 0)
            
    # show random numbers
    print(values)
    
# call main function
main()