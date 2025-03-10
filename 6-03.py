# Write a program that does the following: opens an output file named 
# number_list.txt , applies a loop to write numbers from 1 to 100 to the file, and then closes
# the file

def main():
    # Create file number_list.txt
    my_file = open("number_list.txt","w")
    
    # Write the data to the file 
    for number in range(1,101):
        my_file.write(str(number) + "\n")
    
    file_contents = my_file.read()
    
    #Close the file
    my_file.close()
    
    # Print the data read
    print(file_contents)
    
    
# Call main function
main()