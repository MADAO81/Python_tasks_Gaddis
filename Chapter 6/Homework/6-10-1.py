# Golf score. The amateur golf club holds tournaments every weekend. 
# The president of the club asked you to write two programs: 
# • a program that reads the name of each player and his score in the game, 
# entered from the keyboard, and then saves them as entries in a file golf.txt (each record will have
# a field for the player's name and a field for the player's score);
# • a program that reads records from a golf file.txt and displays them on the screen.

def main():
    # create a variable to control the loop
    another = "y"
    
    # Create file 
    score_file = open("golf.txt", "w")
    
    # add records to file 
    while another == "y" or another == "Y":
        # get data with player and score records
        print("Pleas enter the information about players and their scores:")
        player = input("Enter the name of player: ")
        score = int(input("Enter the scores of player: "))
        
        # add data to file
        score_file.write(player+"\n")
        score_file.write(str(score)+"\n")
        
        # determine if the user wants to add another entry to the file
        print("Do you want to add another data to the file?")
        another = input("Y - for yes, everything else = no: ")
        
    # Close the file 
    score_file.close()
    print("Data added to golf.txt")
    
# call main function
main()
    
    
    