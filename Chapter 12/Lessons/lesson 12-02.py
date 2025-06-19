# This program demonstrates a recursive function.

def main():
    # By passing argument 5 to the message function, we tell it to show the message five times.
    message(5)
    
def message(times):
    if times >0:
        print("This is recursive function!")
        message(times - 1)

    
# call main function
main()