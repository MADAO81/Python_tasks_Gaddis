# The real estate tax.
# The municipal district collects taxes on real estate and property based on the estimated value of the property, 
# which is 60% of its actual value. For example, if an acre of land is valued at $10,000, 
# then its estimated value will be $6,000. In this case, the property tax will be 72 cents for every $100 
# of the assessed value. The tax per acre, estimated
# at $6,000, will be $43.20. Write a program that asks for the actual value of real estate 
# and shows the estimated value and property tax.
ESTIMATED_VALUE_INDEX = 0.6  # index of the estimated value of the property
TAX_INDEX = 0.0072  # tax is 72 cents for every $100 of the price of property


def main():
    property_value = float(input("Enter the value of your property, $: "))
    print(f"Estimated value of your property: $ {estimated_value(property_value):,.2f}")
    print(f"Tax for your property: $ {tax_calc(property_value):,.2f}")


def estimated_value(value):
    estimated_value = value * ESTIMATED_VALUE_INDEX
    return estimated_value


def tax_calc(value):
    tax = estimated_value(value) * TAX_INDEX
    return tax


main()
