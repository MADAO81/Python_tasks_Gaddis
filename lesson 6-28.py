# This program calculates wage before taxes

def main():
    try:
        # Get worked hours
        hours = int(input("How many hours did you work? "))

        # Get hour pay rate
        pay_rate = float(input("Enter hourly pay rate: "))

        # Calculate wage
        gross_pay = hours * pay_rate

        # Show wage
        print(f"Your wage: ${gross_pay:.2f}")
    except ValueError as err:
        print(err)

# Call main function
main()

