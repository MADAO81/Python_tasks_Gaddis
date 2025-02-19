# Car expenses.
# Write a program that asks the user to enter
# monthly expenses for the following needs related to his car: loan payment
# maintenance, insurance, gasoline, engine oil, tires, and maintenance. The program
# should then show the total monthly cost and the total annual cost of these expenses.
MONTHS_QUANTITY = 12

def main():
    loan = float(input("Enter the price of loan: "))
    insurance = float(input("Enter the price of insurance: ")) 
    gasoline = float(input("Enter the price of gasoline: "))
    oil = float(input("Enter the price of engine oil: "))
    tires_tech = float(input("Enter the price of tires and maintenance: "))
    monthly_payments(loan, insurance, gasoline, oil,tires_tech)
    year_payments(loan, insurance, gasoline, oil,tires_tech)
    
def monthly_payments(loan, insurance, gasoline, oil,tires_tech):
    total = loan + insurance + gasoline + oil + tires_tech
    print(f"Montly payments total: $ {total:,.2f}")

def year_payments(loan, insurance, gasoline, oil,tires_tech):
    total = (loan + insurance + gasoline + oil + tires_tech) * MONTHS_QUANTITY
    print(f"Year payments total: $ {total:,.2f}")
    
main()