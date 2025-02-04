#Calories burned
calories_per_minute = 4.2 #calories burned in one minute
calories_overall = 0 #calories counter
for i in range(10,31,5):
    calories_overall = i * calories_per_minute
    print("Calories burned for", i,"minutes:", format(calories_overall, ".2f"))