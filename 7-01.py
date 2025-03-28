# Sales amount. Develop a program that asks the user to enter sales for each day of the week.
# The amounts must be saved in the list. Use a loop to calculate the total sales and display the result.

def main():
    sales = []  # Create an empty list
    sales_amount = 0.0 # Create an empty sum
    while len(sales) != 7:
        day_revenue = input("Enter daily revenue: ")
        sales.append(float(day_revenue))
    print(f"The revenue for each day was ${sales}")
    for daily_revenue in sales:
        sales_amount += daily_revenue
    print(f"Total sales: {sales_amount:,.2f} $")

# Call main function
main()
