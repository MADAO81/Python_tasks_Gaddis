# This program prompts the user to enter sales
# amounts and writes these amounts to the sales.txt file.

def main():
    # Get sale days
    num_days = int(input("How many days of sales "
                         "information do you have? "))

    # Open new file
    sales_file = open("sales.txt", "w")

    # Get sum of sales for each day and write them to the file
    for count in range(1, num_days + 1):
        sales = float(input("Enter the sales for day № " + str(count) + ": "))

        # Write the sum of sales to the file
        sales_file.write(str(sales)+"\n")

    # Close the file
    sales_file.close()
    print("Data write to sales.txt")

main()
