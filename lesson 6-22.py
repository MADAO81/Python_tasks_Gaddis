# This program calculates wages before deductions

def main():
    # Get the worked hours
    hours = int(input("How many hours did you work?"))

    # Get the hour pay rate
    pay_rate = float(input("Enter your hour pay rate: "))

    # Calculate the gross pay
    gross_pay = hours * pay_rate

    # Show wage
    print(f"Your wage is {gross_pay:,.2f}$")

# Call main function
main()