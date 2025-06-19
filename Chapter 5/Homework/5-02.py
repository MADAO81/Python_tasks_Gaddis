# Sales tax. Write a program that will ask the user to enter the purchase amount. 
# The program should then calculate the federal and regional sales tax.
# The federal sales tax is 5%, and the regional tax is 2.5%.
# The program should show the purchase amount, federal sales tax, regional sales tax, 
# total sales tax, and total sales amount (i.e., the purchase amount and total sales tax).
# Put tasks in functions
FEDERAL_TAX_RATE = 0.05
REGIONAL_TAX_RATE = 0.025


def main():
    total_sales = float(input("Enter the sum of sales: "))
    print("Sales before taxes: $ ", format(total_sales, ",.2f"))
    federal_tax(total_sales)
    regional_tax(total_sales)
    total_sales_tax(total_sales)
    sales_amount(total_sales)


def federal_tax(sales):
    fed_tax_sum = sales * FEDERAL_TAX_RATE
    print("Federal tax total: $ ", format(fed_tax_sum, ",.2f"))


def regional_tax(sales):
    reg_tax_sum = sales * REGIONAL_TAX_RATE
    print("Regional tax total: $ ", format(reg_tax_sum, ",.2f"))


def total_sales_tax(sales):
    fed_tax_sum = sales * FEDERAL_TAX_RATE
    reg_tax_sum = sales * REGIONAL_TAX_RATE
    total_tax_sum = fed_tax_sum + reg_tax_sum
    print("Overall tax total: $ ", format(total_tax_sum, ",.2f"))


def sales_amount(sales):
    fed_tax_sum = sales * FEDERAL_TAX_RATE
    reg_tax_sum = sales * REGIONAL_TAX_RATE
    total_tax_sum = fed_tax_sum + reg_tax_sum
    final_result = sales - total_tax_sum
    print("Sales after taxes: $ ", format(final_result, ",.2f"))


main()
