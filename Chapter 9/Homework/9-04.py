# Unique words

def main():
    # get name of input file 
    input_name = input("Enter the name of input file: ")
    
    # open input file 
    input_file = open("data\\", + input_name, "r")
    
    text = input_file.read()
    words = text.split()
    
    # create set of unique words 
    unique_words = set(words)
    
    # print result 
    print("This is unique words in the text: ")
    for word in unique_words:
        print(word)
        
    # close file 
    input_file.close()
    
# call main function 
main()
