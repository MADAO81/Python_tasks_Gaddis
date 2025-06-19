# Write the program that opens the file my_name.txt created 
# by the program in task 1, reads your name from a file, 
# displays the name on the screen, and then closes the file

def main():
    # Open file my_name.txt
    my_file = open("my_name.txt","r")
    
    # Read the contents of file
    file_contents = my_file.read()
    
    #Close the file
    my_file.close()
    
    # Print the data read
    print(file_contents)
    
    
# Call main function
main()
