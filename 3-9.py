pocket_number = int(input("Enter the number that appeared on the roulette wheel : "))

if pocket_number == 0:
    print("Zero! Pocket is green")
elif 1 <= pocket_number <= 10:
    if pocket_number % 2  == 0:
        print("The number is even.Pocket is black!")
    else:
        print("The number is odd.Pocket is red!")
elif 11 <= pocket_number <= 18:
    if pocket_number % 2  == 0:
        print("The number is even.Pocket is red!")
    else:
        print("The number is odd.Pocket is black!")
elif 19 <= pocket_number <= 28:
    if pocket_number % 2  == 0:
        print("The number is even.Pocket is black!")
    else:
        print("The number is odd.Pocket is red!")
elif 29 <= pocket_number <= 36:
    if pocket_number % 2  == 0:
        print("The number is even.Pocket is red!")
    else:
        print("The number is odd.Pocket is black!")
else:
    print("The number is wrong! Enter the correct number!")