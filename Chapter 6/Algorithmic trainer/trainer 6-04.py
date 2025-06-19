# write a program that does the following: opens a file number_list.txt , 
# created by the program that you wrote in task 3, reads all the numbers from the file, 
# displays them on the screen and then closes the file.

def main():
    # Create file number_list.txt
    my_file = open("number_list.txt","w")
    
    file_contents = my_file.read()
    
    # Print the data read
    print(file_contents)
    
    #Close the file
    my_file.close()
    

    
# Call main function
main()
