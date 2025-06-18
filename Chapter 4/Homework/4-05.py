#Average rainfall
all_years = int(input("Enter the number of years of meteorological observations:"))
months_in_year = 12
rainfall_counter_overall = 0 
if all_years > 0:
    for y in range(1, all_years+1):
        rainfall_counter_year = 0
    
        for m in range(1,13):
            rainfall_month = float(input(f"Enter the amount of rainfall in {m} month: "))
            if rainfall_month >= 0:
                rainfall_counter_year += rainfall_month
            else:
                print("Error! Enter the correct data!")
                rainfall_month = float(input(f"Enter the amount of rainfall in {m} month: "))
        print("Rainfall overall in", y ,"year is: ", rainfall_counter_year)
        rainfall_counter_overall +=rainfall_counter_year
    months_overall = all_years * months_in_year
    rainfall_average = rainfall_counter_overall / months_overall
    print("The number of months of meteorological observations: ", months_overall)
    print("Total rainfall : ", rainfall_counter_overall)
    print("Average precipitation over the entire observation period: ", format(rainfall_average, ".2f"))

else:
    print("Error! Enter the correct quantity of years!")