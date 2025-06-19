# Displaying the file numbers.txt on the screen
def main():
    # open file
    file_numbers = open("numbers.txt","r")
    
    file_contents = file_numbers.read()
    
    print(file_contents)
    
    file_numbers.close()
    
main()