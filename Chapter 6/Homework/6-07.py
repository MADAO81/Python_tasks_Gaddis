# a program for writing a file with random numbers(1-500)
import random

def main():
    num_quantity = int(input("Enter the quantity of random numbers in your file: "))
    work_file = open("random_numbers.txt", "w")
    
    # Write numbers to the file
    for count in range(1,num_quantity+1):
        # generate random number
        number = random.randint(1,500)
        # write number to the file 
        work_file.write(str(number) + "\n")
        
    #close file
    work_file.close()
    print("Data written to random_numbers.txt")
    
# Call main function
main()
    