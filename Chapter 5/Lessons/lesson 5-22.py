# This program calculates the selling price of a retail product.

# DISCOUNT_PERCENTAGE used as a global constant for the discount percentage.
DISCOUNT_PERCENTAGE = 0.20

# main function
def main(): 
    # Get the regular price of the product.
    reg_price = get_regular_price()
    
    # Calculate the selling price.
    sale_price = reg_price - discount(reg_price)
    
    # Show the selling price 
    print("Selling price is $", format(sale_price, '.2f'), sep = ' ')
    
# Function 'get_regular_price' prompts the user 
# to enter the regular price of the product and returns this value.
def get_regular_price():
    price = float(input("Enter the regular price: "))
    return price
    
# Function 'discount' accepts the product price as
# an argument and returns the discount amount , 
# specified in DISCOUNT_PERCENTAGE
def discount(price):
    return price * DISCOUNT_PERCENTAGE
    
# Call main function
main()
