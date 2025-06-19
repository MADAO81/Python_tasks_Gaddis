# This program counts the number of occurrences
# of the letter T (in upper or lower case) in a string value

def main():
    # create counter
    count = 0
    
    # get string value from user
    my_string = input("Enter the sentense: ")
    
    # Calculate "T"-letters
    for ch in my_string:
        if ch == "T" or ch == "t":
            count += 1
            
    # print result
    print("T-letter appears", count, "times.")
    
# call main function
main()
    