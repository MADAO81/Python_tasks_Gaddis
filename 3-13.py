cargo_weight = float(input("Enter the weight of your cargo in gramms: "))
price_first_category = 150 # price for 100 gramms of cargo in weight 200 gramms and less
price_second_category = 300 # price for 100 gramms of cargo in weight between 200 and 600 gramms
price_third_category = 400 # price for 100 gramms of cargo in weight between 600 and 1000 gramms
price_fourth_category = 475 # price for 100 gramms of cargo in weight more than 1000 gramms
freight_cost = 0 # Total price of your freigt

if  0 < cargo_weight <= 200:
    freight_cost = (cargo_weight * price_first_category)/100
    print("Total price of your freigt will be: $", format(freight_cost, ",.2f"))
elif 200 < cargo_weight <= 600:
    freight_cost = (cargo_weight * price_second_category)/100
    print("Total price of your freigt will be: $", format(freight_cost, ",.2f"))
elif 600 < cargo_weight <= 1000:
    freight_cost = (cargo_weight * price_third_category)/100
    print("Total price of your freigt will be: $", format(freight_cost, ",.2f"))
elif cargo_weight > 1000:
    freight_cost = (cargo_weight * price_fourth_category)/100
    print("Total price of your freigt will be: $", format(freight_cost, ",.2f"))
else:
    print("Error. Enter the correct data.")