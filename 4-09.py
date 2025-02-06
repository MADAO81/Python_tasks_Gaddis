#Ocean level
annual_increase_level = 1.6
number_of_years = 25
start_level = 0
print("Year\tOcean level increase")
print("==========================")
for i in range(1,number_of_years + 1):
    year_increase_level = i * annual_increase_level
    print(i,format(year_increase_level,".2f"),sep = "\t")
