five_cents_coins = int(input("Enter the quantity of 5-cent coins:"))
ten_cents_coins = int(input("Enter the quantity of 10-cent coins:"))
fifty_cents_coins = int(input("Enter the quantity of 50-cent coins:"))
sum_of_five_cents_coins = five_cents_coins * 5
sum_of_ten_cents_coins = ten_cents_coins * 10
sum_of_fifty_cents_coins = fifty_cents_coins * 50

amount_of_coins = sum_of_five_cents_coins + sum_of_ten_cents_coins + sum_of_fifty_cents_coins

if amount_of_coins/100 == 1:
    print("You win!")
else:
    print("You lose!")