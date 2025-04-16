# A word separator.Write a program that accepts a sentence as input,
# in which all the words are written without spaces, but the first letter of each word is in uppercase. 
# Convert the sentence to a string value in which the words are separated by spaces, 
# and only the first one starts with an uppercase letter.

def main():
    # local valuable
    result = ""
    
    # get users input 
    user_input = input("Enter your message: ")
    
    # Copy the first letter in the string value in uppercase.
    result = result + user_input[0]
    
    for i in range(1, len(user_input)):
        
        ch = user_input[i]
        
       # If the next character is in uppercase, then insert
       #a space for the new word and convert the letter to lowercase.    
        if ch.isupper():
           ch = ch.lower()
           result = result + " "
           
        result = result + ch 
        
    print(result)
    
# call main function
main()