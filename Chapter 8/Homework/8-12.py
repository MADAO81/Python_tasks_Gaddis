# youth jargon

def main():
    # set local valuables
    result = ""
    current_word = ""
    ENDING = "AY"
    
    # get user's input 
    user_string = input("Enter the string value: ")
    
    # separate input sentence to words 
    words = user_string.split()
    
    # loop that changes every word 
    for i in range(len(words)):
        
        item = words[i].upper()
        
        # for one letter words add only ending 
        if len(item) == 1:
            current_word = item + ENDING
            
        # for two and more letter words change order of letters and add ending
        else:
            current_word = item[1:] + item[0] + ENDING
            
        # add changed word to result
        result += current_word
        
        # if there is another one word add whitespace to result
        if i < len(words) + 1:
            result += " "
            
    # show result
    print(result)
    
# call main function
main()