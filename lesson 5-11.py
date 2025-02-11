# This program demonstrates named arguments.

def main():
    """Show the amount of simple interest income using 0.01 as the interest rate for the period
    0.01 as the number of periods and $10 000 as the main amount on the account."""
    show_interest(rate=0.01, periods=10, principal=10000.00)
    
""" Function show_interest shows the amount of simple interest income for the specified 
principal amount, the interest rate for the period, and the number of periods. """

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print("Simple interest income is: $ ",
        format(interest, ',.2f'), sep = '')
    
# Call main function 
main()