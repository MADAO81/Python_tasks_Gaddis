# task 10-08

# CashRegister Class 
from objects import cashRegister # classes are stored in the objects folder

# Constants for the options of the purchased goods
PANTS = 1
SHIRT = 2
DRESS = 3
SOCKS = 4
SWEATER = 5

# main method 
def main():
    
    # create saleable goods 
    pants = retail.RetailItem("Pants", 10, 19.99)
    shirt = retail.RetailItem("Shirt", 15, 12.50)
    dress = retail.RetailItem("Dress", 3, 79.00)
    socks = retail.RetailItem("Socks", 50, 1.00)
    sweater = retail.RetailItem("Sweater", 5, 49.99)
    
    # Create a dictionary of saling goods
    sale_items = {PANTS:pants, SHIRT:shirt, DRESS:dress, SOCKS:socks, SWEATER:sweater}
    
    # create cash register 
    register = cashRegister.CashRegister()
    
    # Initialize the loop check.
    checkout = "N"
    
    # The user wants to purchase additional products:
    while checkout == "N"
        
        user_choice = get_user_choice()
        item = sale_items[user_choice]
        if item.get_inventory() == 0:
            print("This product is out of stock.")
        else:
            register.purchase_item(item)
            
            # Update the product position
            new_item = retail.RetailItem(item.get_description(), item.get_inventory()-1, item.get_price())
            sale_items[user_choice] = new_item
            checkout = input("Are you ready for checkout(y/n)?")
            
    print()
    print("The amount of your purchase is: ", format(register.get_total(), ".2f"))
    print()
    register.show_items()
    register.clear()
    
def get_user_choice():
    print("Menu")
    print("=========================")
    print("1. Pants")
    print("2. Shirt")
    print("3. Dress")
    print("4. Socks")
    print("5. Sweater")
    print()
    
    choice = int(input("Enter the item in the product menu that you would like to purchase: "))
    print()
    
    while choice > SWEATER or choice < PANTS:
        choice = int(input("Enter valid product number: "))
        print()
    
    return choice
    
# call main function
main()