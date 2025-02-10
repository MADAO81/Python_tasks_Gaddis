#Definition of the main function.
def main():
    get_name()
    print("Hello",name) # this calls Error
    
#Definition of the function get_name.
def get_name():
    name = input("Enter your name: ")
    
#Call main function
main()



