# Quiz with State capitals
import random

def main():
    # create dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

        
    # Initialize local valuables
    correct = 0
    wrong = 0
    user_solution = ""
    index = 0
    next_question = True
        
    while next_question:
        # Get access to the list of state names
        state_iterator = iter(capitals)
            
        # Get random name of state for next_question
        index = (random.randint(1,50)-1)
        for i in range(index - 1):
            temp = state_iterator.__next__()
        current_state = str(state_iterator.__next__())
            
        # get user solution 
        user_solution = input("Call state capital " + current_state + " (or press 0 to exit):" )
        
        # user would like to exit the program
        if user_solution == "0":
            next_question = False
            print("You gave", correct,"correct answers and ",wrong, "wrong answers.")
            
        # Correct answer 
        elif user_solution == capitals[current_state]:
            correct += 1 
            print("Correct.")
        # Wrong answer
        else:
            wrong += 1
            print("Wrong!")
            
# call main function
main()
            