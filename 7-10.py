# World Series champions

def main():
    # define variables
    team = " "
    win_count = 0
    
    try:
        # open file to read 
        input_file = open(r"data\WorldSeriesWinners.txt","r")
        
        # read all lines from file to list
        winners = input_file.readlines()
        
        # cut all closing newline chars
        for i in range(len(winners)):
            winners[i] = winners[i].rstrip("\n")
            
        # get data from user
        team = input("Enter the name of the team: ")
        
        # Check if this team won the World Series.
        if team not in winners:
            print("Team", team, "never won Worls Series.")
            
        # Calculate the number of team wins in the World Series
        else: 
            for item in winners:
                if item == team: 
                    win_count += 1 
            print("Team", team, "won World Series", win_count, "times, between 1903 and 2009 years.")
            
    # Handle any errors that may occur
    except IOError:
        print("File not found.")
    except IndexError:
        print("Indexation error.")
    except:
        print("Error occured.")
        
# call main function
main()
    