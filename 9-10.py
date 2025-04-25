# word index 

# The get_word_dict function returns a dictionary containing words 
# from the line_list list as keys and their line numbers as values.
def get_word_dict(line_list):
    # create line counter
    count = 0
    
    # create dictionary for words 
    word_dict = {}
    
    # Bypass the list of lines in the loop
    for e in line_list: 
        # drop line for words
        words = e.split(" ")
        
        # Bypass words list in the loop 
        for w in words: 
            # if word in dictionary....
            if  w in words:
                # update exsisting element 
                word_dict[w].add(count + 1)
            else:
                # Otherwise, save the word in the dictionary.
                word_dict[w] = set([count + 1])
                
        # update counter 
        count += 1 
            
    # return dictionary
    return word_dict
    
# The write_index_file function writes an index file containing the dictionary elements word_dict.
def write_index_file(word_dict):
    # open file 
    outputfile = open(r"data\index.txt", "w")
    
    # record elements of the dictionary
    for key in word_dict:
        # record word 
        outputfile.write(key + ":")
        # record numbers of lines 
        for val in word_dict[key]:
            outputfile.write(str(val) + " ")
        # record new line symbol 
        outputfile.write("\n")
    
    # close file 
    outputfile.close()
    
def main():
    # open file
    inputfile = open(r"data\Kennedy.txt", "r")
    
    # read file content
    line_list = inputfile.readlines()
    
    # close file 
    inputfile.close()
    
    # delete new line symbol from every element of list 
    for i in range(len(line_list)):
        line_list[i] = line_list[i].rstrip("\n")
        
    # get dictionary with words and numbers of lines 
    word_dict = get_word_dict(line_list)
    
    # record index file 
    write_index_file(word_dict)
    
# call main function
main()