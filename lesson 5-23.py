# This program calculates the payment to the seller
def main():
    # Get amount of sales
    sales = get_sales()
    
    # Get amount of prepaid expence
    advanced_pay = get_advanced_pay()
    
    # Determine comission rate 
    comm_rate = determine_comm_rate(sales)
    
    # Calculate salary
    pay = sales * comm_rate - advanced_pay
    
    # Show overall payout
    print("Overall payout is $", format(pay, '.2f'), sep = ' ')
    
    # Determine if the payout is negative.
    if pay < 0:
        print("The seller must refund the difference to the company")
        
# Function get_sales gets the monthly sales 
# of the seller from the user and returns this value.
def get_sales():
    # Get the monthly sales 
    monthly_sales = float(input("Enter the monthly sales: "))
    
    # Return the entered sum
    return monthly_sales
    
# Function get_advanced_pay gets the amount 
# an advance payment to a specific seller
# and returns this amount.
def get_advanced_pay():
    # Get advanced pay 
    print("""Enter the sum of prepaid rate or enter 0,
    if there is no prepaid rate.""")
    advanced = float(input("Prepaid rate: "))
    
    # Return entered sum
    return advanced
    
# Function determine_comm_rate accepts the amount of sales 
# returns the appropriate
# commission rate as an argument.
def determine_comm_rate(sales):
    if sales < 10000.00:
        rate = 0.10
    elif sales>=10000 and sales <= 14999.99:
        rate = 0.12 
    elif sales >=15000 and sales <= 17999.99:
        rate = 0.14 
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
        rate = 0.18 
        
    # Return commisiion rate 
    return rate 

main()
    