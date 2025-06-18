#example of bad data
hours = int(input("Enter the hours worked this week: "))
pay_rate = float(input("Enter the pay rate: "))
gross_pay = hours * pay_rate 
print("The salary is: $",format(gross_pay, ".2f"), sep = " " )