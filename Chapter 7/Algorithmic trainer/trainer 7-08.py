# Constants for rows and colons
ROWS = 5
COLS = 3

def main():
    # Create two dimension list 
    two_dim_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0],[0, 0, 0]]
    
    # Fill the list by user integers
    for r in range(ROWS):
        for c in range(COLS):
            two_dim_list[r][c] = int(input("Enter the integer: "))

    # Show list 
    print(two_dim_list)
    
# call main function
main()