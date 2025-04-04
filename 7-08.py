# Search by name. You have two files "BoyNames.txt", "GirlNames.txt".
# Develop program that read content of files in two lists.
# The user should be able to enter a boy's name, a girl's name, 
# or both names, and the application should display messages 
# indicating that the names entered are among the most popular names.

def main():
    # Define variables
    boy = ''
    girl = ''
    
    try:
        # Open file to read 
        boy_input = open("BoyNames.txt", "r")
        
        # Read all lines from the file to list 
        popular_boys = boy_input.readlines()
        
        # Cut "\n" symbol from end of all elements
        for i in range(len(popular_boys)):
            popular_boys[i] = popular_boys[i].rstrip('\n')
            
        # Open file to read 
        girl_input = open("GirlNames.txt", "r")
        
        # Read all lines from file to list 
        popular_girls = girl_input.readlines()
        
        # Cut "\n" symbol from end of all elements 
        for i in range(len(popular_girls)):
            popular_girls[i] = popular_girls[i].rstrip('\n')
            
        # Get data from user
        boy = input("Enter a boy's name or N, if you don't want to enter boy's name:")
        girl = input("Enter a girl name or N, if you don't want to enter girl's name:")
        
        # Show result for entered male name 
        if boy == "N":
            print("You decided to not enter the boy's name. ")
        elif boy in popular_boys:
            print(boy, "is one of the popular male names.")
        else:
            print(boy, "is not a popular male name.")
            
        # Show result for entered female name
        if girl == "N":
            print("You decided to not enter the girl's name.")
        elif girl in popular_girls:
            print(girl, "is one of the popular female names.")
        else:
            print(girl,"is not a popular female name.")
            
    # Handle any errors that may occur
    except IOError:
        print("File not found.")
    except IndexError: 
        print("Error of indexation.")
    except:
        print("Error occured.")
        
# Call main function
main()
        
        