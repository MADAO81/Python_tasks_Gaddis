# Symbols analize

def main():
    num_upper_letters = 0
    num_lower_letters = 0
    num_numbers = 0
    num_whitespaces = 0
    words = []
    

    infile = open(r"data\text.txt", "r")
        
    # read data to the list
    sentences = infile.read()
        
    for ch in sentences:
        if ch.isupper():
            num_upper_letters +=1
        if ch.islower():
            num_lower_letters +=1
        if ch.isdigit():
            num_numbers +=1
        if ch.isspace():
            num_whitespaces +=1
   
    # Close file
    infile.close()
        
    # Show result
    print("Average number of letters in upper register in file: ", num_upper_letters)
    print("Average number of letters in lower  register in file: ", num_lower_letters)
    print("Average number of digits in file: ", num_numbers)
    print("Average number of whitespaces in file: ", num_whitespaces)
        
      
        

# call main function
main()
    