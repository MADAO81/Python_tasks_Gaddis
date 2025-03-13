# write a program that opens the output file. number_list.txt , 
# but does not erase the contents of the file if it already exists.

def main():
    # Open file number_list.txt
    my_file = open("number_list.txt","а")
    # Read the contents of file
    file_contents = my_file.read()
    
    # Close the file 
    my_file.close()
    
    # Print the data read into RAM
    print(file_contents)

    
# Call main function
main()
