year = int(input("Enter the year number: "))
if year % 100 == 0 and year % 400 == 0:
    print("The year is leap.")
elif year % 100 != 0 and year % 4 == 0:
    print("The year is leap.")
else:
    print("The year is not leap.")