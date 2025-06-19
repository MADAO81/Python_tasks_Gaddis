# What is the price of insurance?
# Many financial experts recommend that 
# real estate owners should insure their homes or buildings for at least 80%
# of the replacement cost. Write a program that asks the user to enter
# the cost of a building and then shows the minimum insurance amount for which he
# must insure real estate.
REPLACEMENT_COST_INDEX = 0.8  # global variable. the amount of damage compensation


def main():
    cost_of_ownership = float(input("Enter the market value of your property: "))
    ins_sum_calc(cost_of_ownership)


def ins_sum_calc(cost):
    insurance_payment = cost * REPLACEMENT_COST_INDEX
    print(f"Insurance payment total: $ {insurance_payment:,.2f}")


main()
