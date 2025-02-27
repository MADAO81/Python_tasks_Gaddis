# This program receives three names from the user and writes them to a file.

def main():
    # Get 3 names
    print("Enter the names of 3 friends. ")
    name1 = input("Friend #1: ")
    name2 = input("Friend #2: ")
    name3 = input("Friend #3: ")
    
    # Open the file friends.txt 
    myfile = open("friends.txt", "w")
    
    # Write the names to the file
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')
    
    # Close the file
    myfile.close()
    print("Names were written to the file friends.txt ")

# Call main function    
main()