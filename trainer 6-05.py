# change the program that you wrote in
# task 4 so that it summarizes all the numbers 
# read from the file and displays their sum on the screen.

def main():
    # Open file number_list.txt
    my_file = open("number_list.txt","r")
    total = 0 # Initialize storage
    for num in my_file:
        num = int(my_file.readline())
        total += num
    #Close the file
    my_file.close()
    
    print("Sum of numbers in the file: ", total)
    

    
# Call main function
main()
