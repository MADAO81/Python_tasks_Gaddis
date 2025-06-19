# This program shows step-by-step instructions
# for disassembling the  clothes dryer "ACME".
# The main function performs the main logic of the program.
def main():
    # Show start message.
    startup_message()
    input("Press Enter to see Step 1.")
    # Show Step 1 
    step1()
    input("Press Enter to see Step 2.")
    # Show Step 2
    step2()
    input("Press Enter to see Step 3.")
    # Show Step 3 
    step3()
    input("Press Enter to see Step 4.")
    # Show Step 4
    step4()
    
# Function startup_message shows
# start message on the screen.
def startup_message():
    print("This program shows solutions")
    print("to disassembling clothes dryer ACME.")
    print("This process consists of 4 steps.")
    print()
    
# Function step1 shows instructions for Step 1
def step1():
    print("Step 1: Turn off the dryer and move it away from the wall.")
    print()
    
# Function step2 shows instructions for Step 2
def step2():
    print("Step 2: Remove the six screws from the back of the dryer.")
    print()

# Function step3 shows instructions for Step 3
def step3():
    print("Step 3: Remove the back panel of the dryer")
    print()

# Function step4 shows instructions for Step 4
def step4():
    print("Step 4: Remove the upper block of the dryer")
    print()

# Call the main function to start the program.
main()




