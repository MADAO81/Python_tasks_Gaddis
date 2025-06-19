# The average number of words.

def main():
    # Local valuables
    num_sentences = 0
    total_words = 0
    average_words = 0.0
    words = []
    
    try:
        # Open file text.txt for read 
        infile = open(r"data\text.txt", "r")
        
        # Read data to the list 
        sentences = infile.readlines()
        
        # Quantity of sentences is equal to length of list 
        num_sentences = len(sentences)
        
        # Quantity of values in every list is Quantity of words in every sentence
        for item in sentences:
            words = item.split()
            total_words += len(words)
        
        # Calculate words average 
        average_words = float(total_words)/ num_sentences
        
        # Show words average
        print("Average number of words per line: ", average_words)
        
        # Close file
        infile.close()
        
    # Handle any errors that may occur
    except IOError:
        print("Error occured while opening the file.")
    except:
        print("Error occured.")
        
# call main function
main()
    