mark_up = 2.5
another = "y"

while another == "y" or another == "Y":
    wholesale = float(input("Enter the wholesale price of the product: "))
    
    while wholesale < 0:
        print("Error! The price can not be less than zero")
        wholesale = float(input("Enter the correct price: "))
    
    retail = wholesale * mark_up
    
    print("Retail price is: $", format(retail, ".2f"), sep = " ")
    
    another = input("Is there another item? Enter y if yes) :")