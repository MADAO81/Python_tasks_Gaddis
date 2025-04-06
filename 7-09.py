# Population data
def main():
    # define variables
    yearly_change = []
    change = 0.0
    total_change = 0.0
    average_change = 0.0
    greatest_increase = 0.0
    smallest_increase = 0.0
    greatest_year = 0
    smallest_year = 0

    # Constant for base year
    BASE_YEAR = 1950

    try:
        # Open file to read
        input_file = open(r'data\USPopulation.txt', 'r')

        # Read all lines from file to list
        yearly_population = input_file.readlines()

        # Convert strings to numerals
        for i in range(len(yearly_population)):
            yearly_population[i] = float(yearly_population[i])

        # Calculate change of population for every two years
        for i in range(1, len(yearly_population)):
            change = yearly_population[i] -yearly_population[i-1]
            yearly_change.append(change)

            # If it is the first year, give to variables this year values
            if i == 1:
                greatest_increase = change
                smallest_increase = change
                greatest_year = 1
                smallest_year = 1

            # if it is not first change of population. Renew variables
            else:
                if change > greatest_increase:
                    greatest_increase = change
                    greatest_year = i

                elif change < smallest_increase:
                    smallest_increase = change
                    smallest_year = i

        total_change = float(sum(yearly_change))
        average_change = total_change / len(yearly_change)

        print(f"Average annual change in population for this period is:{average_change:,.2f}")
        print("Year with max population increase:", BASE_YEAR + greatest_year)
        print("Year with min population increase:", BASE_YEAR + smallest_year)

    # Handle errors
    except IOError:
        print("File not found.")
    except IndexError:
        print("Indexation error.")
    except:
        print("Error occured.")


# call main function
main()










