error_counter = 0
day = 0
while day !=5:
    day_error = int(input("Enter the quantity of today errrors: "))
    if day_error >= 0:
        day +=1
        error_counter += day_error
    else:
        print("Invalid data. Enter the correct number.")
print("Total errors accumulated in five days:", error_counter)