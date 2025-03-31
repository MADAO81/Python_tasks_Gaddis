# Rainfall Statistics. Design a program that allows the user to list the total
# rainfall for each of 12 months. The program should calculate and display the
# total rainfall for the year, the average monthly rainfall, and the months with
# the highest and lowest rainfall.

def main():
    # Variables
    total_rainfall = 0.0
    average_rainfall = 0.0
    highest_rainfall = 0.0
    lowest_rainfall = 0.0
    month_lowest = ''
    month_highest = ''
    # Initialize lists
    rainfall = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    months = ["January", "February", "March", "April", "May",
              "June", "July", "August", "September", "October",
                                                     "November", "December"]
    # Get rainfall for every month
    for i in range(12):
        rainfall[i] = float(input("Enter the rainfall for " + months[i] + ":"))

    # Get total rainfall
    total_rainfall = sum(rainfall)

    # Get average
    average_rainfall = total_rainfall / 12

    highest_rainfall = max(rainfall)
    month_highest = rainfall.index(highest_rainfall)

    lowest_rainfall = min(rainfall)
    month_lowest = rainfall.index((lowest_rainfall))

    print(f"Total rainfall in the year: {total_rainfall:,.2f} ")
    print(f"Average rainfall: {average_rainfall:,.2f}")
    print("Maximum value of rainfall:", highest_rainfall, "in", months[month_highest])
    print("Minimal value of rainfall:", lowest_rainfall, "in", months[month_lowest])


main()