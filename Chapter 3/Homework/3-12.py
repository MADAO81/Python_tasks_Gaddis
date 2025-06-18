retail_price = 99.00
units_purchased = int(input("How many units of software you've bought? :"))
first_column_discount = 0.1
second_column_discount = 0.2
third_column_discount = 0.3
fourth_column_discount = 0.4
total_amount = 0
if 0 <= units_purchased <= 9:
    total_amount = units_purchased * retail_price
    print("Total to pay: $", format(total_amount,",.2f"))
elif 10 <= units_purchased <= 19:
    total_amount = units_purchased * (retail_price - (retail_price * first_column_discount)) 
    print("Total to pay: $", format(total_amount,",.2f"))
elif 20 <= units_purchased <= 49:
    total_amount = units_purchased * (retail_price - (retail_price * second_column_discount)) 
    print("Total to pay: $", format(total_amount,",.2f"))
elif 50 <= units_purchased <= 99:
    total_amount = units_purchased * (retail_price - (retail_price * third_column_discount)) 
    print("Total to pay: $", format(total_amount,",.2f"))
elif  units_purchased >= 100:
    total_amount = units_purchased * (retail_price - (retail_price * fourth_column_discount)) 
    print("Total to pay: $", format(total_amount,",.2f"))
else:
    print("Error! Enter the correct quantity!")