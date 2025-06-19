# Golf score. The amateur golf club holds tournaments every weekend. 
# The president of the club asked you to write two programs: 
# • a program that reads the name of each player and his score in the game, 
# entered from the keyboard, and then saves them as entries in a file golf.txt (each record will have
# a field for the player's name and a field for the player's score);
# • a program that reads records from a golf file.txt and displays them on the screen.

def main():

    # Open file to read 
    score_file = open("golf.txt", "r")
    
    # read the field with description of first record
    description = score_file.readline()
    
    # read the last of file
    while description !="":
        # read the field with scores
        scores = float(score_file.readline())
        
        # delete \n from description
        description = description.rstrip("\n")
        
        # show record
        print("Player: ",description)
        print("Score: ", scores)
        
        # read the next description
        description = score_file.readline()
        
    # close file
    score_file.close()

# call main function
main()

    
    