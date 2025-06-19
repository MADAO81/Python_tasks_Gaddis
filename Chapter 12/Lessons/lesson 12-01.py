# This program demonstrates a recursive function.

def main():
    message()
    
def message():
    print("This is recursive function!")
    message()
    
# call main function
main()