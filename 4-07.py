#A small coin for a salary

work_days = int(input("Enter your working days: "))
daily_payout = 1 #first day payout in cents
salary = 0

for i in range(2,work_days+1):
    daily_payout = daily_payout * 2
    salary += daily_payout
salary_overall = (salary + 1)/100 
print("Your salary: $", salary_overall)