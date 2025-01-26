books_bought = int(input("How many books have you bought this month?"))
earned_points = 0
if  0 <= books_bought <= 1:
    earned_points = 0
    print("You've earned", earned_points,"points!")
elif  2 <= books_bought <= 3:
    earned_points = 5
    print("You've earned", earned_points,"points!")
elif  4 <= books_bought <= 5:
    earned_points = 15
    print("You've earned", earned_points,"points!")
elif  6 <= books_bought <= 7:
    earned_points = 30
    print("You've earned", earned_points,"points!")
elif books_bought >= 8:
    earned_points = 60
    print("You've earned", earned_points,"points!")