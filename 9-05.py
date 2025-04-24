# Frequency of words.

def main():
    # create an empty dictionary
    counter = {}
    
    # get input text 
    input_name = input("Enter the name of input file: ")
    input_file = open("data\\" + input_name, "r")
    
    text = input_file.read()
    words = text.split()
    
    # Add every unique word to the dictionary with counter 0
    unique_words = set(words)
    for word in unique_words:
        counter[word] = 0
        
    # for every word in text increase it's counter in the dictionary
    for item in words:
        counter[item] += 1
        
    # show result
    print(format("word","15"),"\t", format("appearances", "15"))
    print("---------------------------------------------------")
    while len(counter)>0:
        
        pair = counter.popitem()
        print(format(pair[0],"15"), format(pair[1],"15"))
        
# call main function
main()