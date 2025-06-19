# Monthly sales tax.
# The retail company must file a monthly sales tax report indicating the total sales tax 
# for the month and the amounts charged. 
# municipal and federal sales taxes. The federal sales tax is 5%, and the municipal sales tax is 2.5%. 
# Write a program that asks the user to enter the total sales for the month. 
# From this value, the application should calculate and show
# • the amount of municipal sales tax; 
# • the amount of federal sales tax; 
# • Total sales tax (municipal plus federal).    
MUN_TAX_RATE = 0.025
FED_TAX_RATE = 0.05


def main():
    sales = float(input("Eter the sum of monthly sales, $: "))
    total_tax = fed_tax(sales) + mun_tax(sales)
    print(f"Municipal tax for your sales: $ {mun_tax(sales):,.2f}")
    print(f"Federal tax for your sales: $ {fed_tax(sales):,.2f}")
    print(f"Total tax for your sales: $ {total_tax:,.2f}")


def fed_tax(sales):
    federal_tax_sum = sales * FED_TAX_RATE
    return federal_tax_sum


def mun_tax(sales):
    mun_tax_sum = sales * MUN_TAX_RATE
    return mun_tax_sum


main()
