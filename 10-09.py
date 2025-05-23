# task 10-09

# Quiz

# import question  
from objects import question # the class is stored in the objects folder

def main():
    # local valuables 
    first_points = 0 
    second_points = 0 
    player = ""

    # create question list
    questions = get_questions()
    
    for i in range(10):
        
        if i % 2 == 0:
            player = "One"
        else:
            player = "Two"
            
        print("Question for player ", player, ":")
        
        current = questions[i]
        print(current)
        user_answer = int(input("Enter your solution (number between 1 and 4): "))
        if current.isCorrect(user_answer):
            if player == "One":
                first_points +=1 
            else:
                second_points +=1
            print("This answer is correct!")
            print()
        else:
            print("Incorrect. Correct answer is ", current.get_solution())
            print()
            
    print("First player gain", first_points, "points.")
    print("Second player gain", second_points, "points.")
    if first_points == second_points:
        print("Draw.")
    elif first_points > second_points:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
      
def get_questions():
    
    questions = []
    
    # Create a dictionary of questions and add it to the list.
    question2 = question.Question("How many days are there in a lunar year?", "354", "365","243","379",1)
    questions.append(question1)
    question2 = question.Question("What is the largest planet?", "Mars", "Jupiter", "Earth", "Pluto", 2)
    questions.append(question2)
    question3 = question.Question("Which whale is the biggest?", "Killer whale", "The Humpback Whale", "Beluga", "The Blue Whale", 4)
    questions.append(question3)
    question4 = question.Question("What kind of dinosaur could fly?", "Triceratops", "Tyrannosaurus Rex", "Pteranodon", "Diplodocus", 3)
    questions.append(question4)
    question5 = question.Question("Which of the penguins is the largest?", "Antarctic", "Golden-haired", "Emperor","Whitewing", 3)
    
    return questions 
    
# call main function 
main()
