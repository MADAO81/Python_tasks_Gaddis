# Future value.
# Let's assume that you have a certain amount of money 
# in your savings account, and the account generates a compound monthly interest income. 
# You want to calculate the amount you will have after a certain number of months. 
# The formula is given below:
# F = P *((1 + i/t)**2)
# where F is the future amount in the account after the specified time period; 
# P is the current amount in the account; 'i' is the monthly interest rate; t is the number of months.
# Write a program that prompts the user to enter the current amount in the account, the monthly interest rate, 
# and the number of months the money
# will be in the account. The program must pass these values to a function that returns 
# the future amount in the account after a specified number of months. The program should show the future amount on the account.

def main():
    current_amount = float(input("Enter the amount on your account: "))
    interest_rate = float(input("Enter the monthly interest rate: "))
    deposit_period = int(input("Enter the period(months) of your deposit: "))
    future_amount = deposit_amount(current_amount, interest_rate, deposit_period)
    print(f"Your future amount will be $ {future_amount:,.2f}")

def deposit_amount(current,rate,period):
    future_amount = current * ((1 + rate/period)**2)
    return future_amount
    
main()