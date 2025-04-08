# The Luo Shu Magic Square.

# Global constants
ROWS = 3 # number of rows
COLS = 3 # number of colons
MIN = 1  # minimal number in square
MAX = 9  # max number in square 

def main():
    # create a two-dimensional list
    test_list = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

    # Show this list
    display_square_list(test_list)
    
    # determine if the list is a magic square
    if is_magic_square(test_list):
        print("This is the Luo Shu Magic Square!")
    else:
        print("This is not the Luo Shu Magic Square...")
        
# Function "display_square_list" gets two-dimensional list as argument
# and shows it's values
def display_square_list(value_list):
    for r in range(ROWS):
        for c in range(COLS):
            print(value_list[r][c], end = " ")
        print()
        
# Function "is_magic_square" gets two-dimensional list as argument
# and returns "True" if the list meets all the requirements for a magic square.
def is_magic_square(value_list):
    # Initially assign a value to the state "False"
    status = False
    
    # call functions and save values from them
    is_in_range = check_range(value_list)
    is_unique = check_unique(value_list)
    is_equal_rows = check_row_sum(value_list)
    is_equal_cols = check_col_sum(value_list)
    is_equal_diag = check_diag_sum(value_list)
    
    # Determine if the list meets all the requirements
    if is_in_range and \
       is_unique and \
       is_equal_rows and \
       is_equal_cols and \
       is_equal_diag:
           
           # If yes, than give status = True
           status = True
           
    # Return status
    return status
    
# Function "check_range" gets two-dimensional list as argument
# and returns True, if values is in specified range
def check_range(value_list):
    # Initially assign a value to the state "True"
    status = True
    
    # Iterate through all the values in the list
    for r in range(ROWS):
        for c in range(COLS):
            #Determine if there are any values that are outside the range.
            if value_list[r][c] < MIN or value_list[r][c] > MAX:
                # if yes, than give status = False
                status = False
                
                       
    # Return status
    return status
    
# Function check_unique gets gets two-dimensional list as argument
# and returns True, if values in list are unique 
def check_unique(value_list):
    # Initially assign a value to the state "True"
    status = True
    # Initialize value with desired 
    search_value = MIN 
    # Initialize counter
    count = 0
    
    # Perform a search until the minimum value 
    # is reached and the values are unique.
    while search_value <= MAX and status == True:
        # iterate through all the values in the list
        for r in range(ROWS):
            for c in range(COLS):
                # Determine whether the current value is equal to the desired value.
                if value_list[r][c] == search_value:
                    count +=1 
                # Determine whether count more than 1 
                if count > 1:
                    # If yes, than value not unique, give status False
                    status = False
                    
        search_value += 1 
        # reset the count
        count = 0
        
    # Return status
    return status

# The check_row_sum function accepts a two-dimensional list
# as an argument and returns True if the sum
# The number of values in each row of the list is the same.
# Otherwise, it returns False.  
def check_row_sum(value_list):
    # Initially assign the value True to the state
    status = True
    
    # Calculate sum in first row 
    sum_row_0 = value_list[0][0] + value_list[0][1] + value_list[0][2]
    
    # Calculate sum in second row 
    sum_row_1 = value_list[1][0] + value_list[1][1] + value_list[1][2]
    
    # Calculate sum in third row 
    sum_row_2 = value_list[2][0] + value_list[2][1] + value_list[2][2]
    
    # Determine if the sum of any row is the same.
    if (sum_row_0 != sum_row_1) or (sum_row_0 != sum_row_2) or (sum_row_1 != sum_row_2):
        # if yes set status False
        status = False
        
    # return status
    return status
    
# The check_col_sum function accepts a two-dimensional list
# as an argument and returns True if the sum 
# The number of values in each column of the list is the same.
# Otherwise, it returns False.
def check_col_sum(value_list):
    # Initially assign the value True to the state
    status = True
    
    # Calculate sum in first colon
    sum_col_0 = value_list[0][0] + value_list[1][0] + value_list[2][0] 
    
    # Calculate sum in second colon
    sum_col_1 = value_list[0][1] + value_list[1][1] + value_list[2][1] 
    
    # Calculate sum in third colon
    sum_col_2 = value_list[0][2] + value_list[1][2] + value_list[2][2]
    
    # Determine if the sum of any column is the same.
    if (sum_col_0 != sum_col_1) or (sum_col_0 != sum_col_2) or (sum_col_1 != sum_col_2):
        # If yes, set the status variable to False.
        status = False
    
    # Return status
    return status
    
# The check_diag_sum function accepts a two-dimensional list
# as an argument and returns True if the sum
# The number of values in each diagonal of the list is the same.
# Otherwise, it returns False.
def check_diag_sum(value_list):
    # Initially assign the value True to the state
    status = True
    
    # Calculate sum of first diagonal 
    sum_diag_0 = value_list[0][0] + value_list[1][1] + value_list[2][2]
    
    # Calculate sum of second diagonal     
    sum_diag_1 = value_list[2][0] + value_list[1][1] + value_list[0][2]
    
    # Determine if the sum of the diagonals is the same
    if sum_diag_0 != sum_diag_1:
        status = False
        
    # Return status
    return status
    
# call main function
main()
        
        