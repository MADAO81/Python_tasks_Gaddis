# Population

population = int(input("Enter the starting number of creatures: "))
daily_increase = int(input("Enter the percentage of daily increase of population: "))
days_breeding = int(input("Enter the number of the days for breeding: "))

print("Day\tPopulation")
print("==================")

for i in range(1, days_breeding+1):
    print(i, format(population,",.2f"), sep = "\t")
    population = population + population * (daily_increase/100)

    
    