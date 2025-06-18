# Population

population = int(input("Enter the starting number of creatures: "))
daily_increase = int(input("Enter the percentage of daily increase of population: "))
days_breeding = int(input("Enter the number of the days for breeding: "))
counter = 1

print("Day\tPopulation")
print("==================")

#for i in range(1, days_breeding+1):
#    print(i, format(population,",.2f"), sep = "\t")
#    population = population + population * (daily_increase/100)

while counter != days_breeding + 1:
    print(counter, format(population,",.2f"), sep = "\t")
    population = population + population * (daily_increase/100)
    counter +=1
    
    
    