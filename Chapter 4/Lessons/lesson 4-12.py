#This program calculates the sum of numbers entered by the user.
quantity = 5 #The quantity of numbers will be entered

#Initialize the accumulating variable
total = 0.0

#Explain what we are doing.
print("This program calculates the sum of")
print(quantity," numbers that you will enter.")

#Get the numbers and accumulate them
for counter in range(quantity):
    number = int(input("Enter the number: "))
    total = total + number

#Show the sum of the numbers.
print("The sum of the numbers will be:", total)