# World Series Winners
BASE_YEAR = 1903

def main():
    year_dict = {}
    count_dict = {}
    
    # open file for read 
    input_file = open(r"data\WorldSeriesWinners.txt", "r")
    
    # read all lines to list 
    winners = input_file.readlines()
    
    # fill dictionaries by information
    for i in range(len(winners)):
        team = winners[i].rstrip("\n")
        
        # Find out which year the team became the winner.
        year = BASE_YEAR + i 
        if year >= 1994:
            year += 1 
        if year >= 1994:
            year += 1 
            
        # Add information to the dictionary year_dict 
        year_dict[str(year)] = team 
        
        # renew count_dict
        if team in count_dict:
            count_dict[team] += 1
        else: 
            count_dict[team] = 1 
            
    # Get input data from the user
    year = input("Enter the year in the range 1903-2009: ")
    
    # print result
    if year == "1904" or year == "1994":
        print ("The World Series was not played in ", year)
    elif year< "1903" or year > "2009":
        print("Data for year", year,"is not in data base.")
    else:
        winner = year_dict[year]
        wins = count_dict[winner]
        print("The team that won the World Series in", year, "was", winner, ".")
        print("They won the World Series", wins, "times. ")
        
# call main function
main()