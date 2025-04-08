# magic ball

import random

def main():
    # open file with answers
    response_file = open(r"data\8_ball_responses.txt", "r")
    
    # read content of file to list
    responses = response_file.readlines()
    
    # close file
    response_file.close()
    
    # cut off  new line symbol from every element
    for i in range(len(responses)):
        responses[i] = responses[i].rstrip("\n")
        
    # get a question from user
    question = input("Enter your question: ")
    
    # show random answer 
    print(responses[random.randint(0,len(responses))])

# call main function
main()