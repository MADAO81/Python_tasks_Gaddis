#This program demonstrates what happens when you change the value of a parameter.

def main():
    value = 99
    print("Value is: ", value)
    change_me(value)
    print("After returning to the function 'main' value is: ", value)

def change_me(arg):
    print("I am changing value.")
    arg = 0
    print("Now value is:", arg)
    
# Call main function
main()