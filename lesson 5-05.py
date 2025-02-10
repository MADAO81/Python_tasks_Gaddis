# This program demonstrates two functions that have local variables with the same names.

def main():
    # Call function 'texas'.
    texas()
    # Call function 'california'.
    california()
    
# Definition of function 'texas'. It creates local variable with name 'birds'
def texas():
    birds = 5000
    print("In Texas lives", birds, "birds.")
    
# Definition of function 'california'. It creates local variable with name 'birds' too.
def california():
    birds = 8000
    print("In California lives", birds, "birds.")
    
# Call main function
main()
    

