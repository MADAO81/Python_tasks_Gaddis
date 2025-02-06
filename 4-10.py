#Rising study fees
study_years = 5
semester_in_year = 2
semester_price = 45000.00
annual_price_increase = 1.03
total_study_cost = 0 


print("Semester\tStudy price")
print("==========================")
semester_overall = study_years * semester_in_year

for i in range(1,semester_overall + 1):
    total_study_cost += semester_price
    print(i, format(semester_price,",.2f"),sep= "\t\t")
    semester_price *= annual_price_increase

print("==========================")    
print("Total cost of study: RR",format(total_study_cost,",.2f") )