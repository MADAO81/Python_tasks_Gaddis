# This program receives a series of lab scores and 
# calculates the average score, discarding the lowest.

def main():
    # get scores from student
    scores = get_scores()
    
    # get sum of scores 
    total = get_total(scores)
    
    # get lowest scores 
    lowest = min(scores)
    
    # minus lowest scores 
    total -= lowest
    
    # calculate average scores. 
    # Note that we divide by the number of grades minus 1, 
    # because the lowest grade was discarded.
    average = total / (len(scores) - 1)
    
    # show average values
    print("The average score, taking into account the discarded lowest score, is ", average)
    

# The get_scores function receives
# a series of ratings from the user and stores them in a list.  
# The specified function returns a link to the list.
def get_scores():
    # create empty list
    test_scores = []
    
    # create variable to manage cycle
    again = "y"
    
    # get scores from user and add it to the list
    while again == "y":
        # get scores from user and add it to the list
        value =float(input("Enter the scores: "))
        test_scores.append(value)
        
        # Would you like to add one more?
        print("Would you like to add one more scores?")
        again = input("y = yes, all the rest = no: ")
        print()
    
    # return list
    return test_scores
    
    
# function get_total takes list as argument and returns sum of values in list
def get_total(value_list):
    # create variable to use it as storage
    total = 0.0
    
    # calculate sum of list elements
    for num in value_list: 
        total += num
        
    # return sum 
    return total
    

# call main function
main()