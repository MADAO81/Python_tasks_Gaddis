# This program demonstrates "in" operator in relation to list

def main():
    # Create list of product numbers 
    prod_nums = ["V475", "F987", "Q143", "R688"]
    
    # Get required product number
    search = input("Enter the product number: ")
    
    # Determine that the number is in list
    if search in prod_nums: 
        print(search, "found in the list")
    else:
        print(search, "not found in the list")
        

# call main function
main()