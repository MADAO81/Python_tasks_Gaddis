# This program demonstrates the conversion of numeric values to 
# string values before writing them to a text file.

def main():
    # Open the file to write
    outfile = open("numbers.txt", "w")
    
    # Get three numbers from User
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter one more number: "))
    num3 = int(input("Enter one more number: "))
    
    # Write this numbers to the file 
    outfile.write(str(num1) + "\n")
    outfile.write(str(num2) + "\n")
    outfile.write(str(num3) + "\n")
    
    # Close file
    outfile.close()
    print("Data written to numbers.txt")
    
# Call main function
main()