# This program adds records of coffee stocks to coffee.txt file
def main():
    # Create a variable to control the loop.
    another = "y"

    # Open file in append mode.
    coffee_file = open("coffee.txt", "a")

    # Add records to file
    while another == "y" or another == "Y":
        # Get data with a coffee record.
        print("Please enter the following information about your coffee: ")
        descr = input("Description: ")
        qty = int(input("Quantity(pounds): "))

        # Add data to file
        coffee_file.write(descr + "\n")
        coffee_file.write(str(qty) + "\n")

        # Determine if the user wants to add another entry to the file.
        print("Do you want to add another data to the file? ")
        another = input("Y - for yes, everything else = no: ")

    # Close the file
    coffee_file.close()
    print("Data added to coffee.txt")


# Call main function
main()
