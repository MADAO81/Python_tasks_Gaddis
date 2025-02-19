#Calories from fats and carbohydrates.
# A nutritionist works at a sports club and gives 
# recommendations to clients regarding diet. As part of his recommendations, 
# He asks clients for the number of grams of fats and carbohydrates they consumed per day. 
# Then, based on the formula below, he calculates the number of calories that
# result from eating fat.:calories from fats = grams of fats * 9
# Then, based on another formula, he calculates the number of calories he gets
# as a result of eating carbohydrates: calories from carbohydrate = grams of carbohydrate * 4
# The nutritionist asks you to write a program that performs these calculations.
def main():
    fat = float(input("Enter the grams of fats, that you got during the day: "))
    carbs = float(input("Enter the grams of carbohydrates, that you got during the day: "))
    cal_overall = carb_cal_calc(carbs) + fat_cal_calc(fat)
    print(f"You got {fat_cal_calc(fat):,.2f} calories from {fat} grams of fat today.")
    print(f"You got {carb_cal_calc(carbs):,.2f} calories from {carbs} grams of carbohydrates today.")
    print(f"You got {cal_overall:,.2f} calories overall today.")
    
def fat_cal_calc(fat):
    fat_calories = fat *9
    return fat_calories
    
def carb_cal_calc(carbs):
    carb_calories = carbs * 6
    return carb_calories
    
main()