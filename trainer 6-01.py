# Write a program that opens the output file. my_name.txt writes your
# name in it and then closes it.

def main():
    # Create file my_name.txt
    my_file = open("my_name.txt","w")
    
    # Write name to the file
    my_file.write("John Doe")
    
    #Close the file
    my_file.close()
    
# Call main function
main()
