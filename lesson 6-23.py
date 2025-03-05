# This program calculates wages before deductions

def main():
    while True:
        try:
            # Get the worked hours
            hours = int(input("How many hours did you work?"))

            # Get the hour pay rate
            pay_rate = float(input("Enter your hour pay rate: "))

            # Calculate the gross pay
            gross_pay = hours * pay_rate

            # Show wage
            print(f"Your wage is {gross_pay:,.2f}$")

        except ValueError:
            print("ERROR: Hours worked and hourly pay rate  must be valid numbers")

# Call main function
main()