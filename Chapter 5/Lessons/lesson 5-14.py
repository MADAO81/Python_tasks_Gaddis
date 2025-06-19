# Create a global variable.
number = 0
def main():
    global number
    number = int(input("Enter the number: "))
    show_number()
    
def show_number():
    print("You have entered the number: ", number)
    
# Call main function
main()