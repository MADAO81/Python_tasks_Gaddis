weight = float(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in metres:"))
body_mass_index = weight / height

if body_mass_index < 18.5:
    print("Your BMI is:",format(body_mass_index,".2f"),". Your weight is below normal")
elif 18.5 <= body_mass_index <= 25:
    print("Your BMI is:",format(body_mass_index,".2f"),". Your weight is normal")
elif  body_mass_index > 25:
    print("Your BMI is:",format(body_mass_index,".2f"),". Your weight is more than normal")
