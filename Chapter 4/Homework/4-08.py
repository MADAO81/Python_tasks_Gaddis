#The sum of the numbers.
number_accumulator = 0
user_number = float(input("""Enter the number. If you want to stop entering numbers, 
enter a negative number."""))
if user_number > 0:
    while user_number > 0:
        user_number = float(input("""Enter the number. If you want to stop entering numbers, 
enter a negative number."""))
        number_accumulator += user_number
else:
    print("The operation was terminated at your request.")
print("The sum of the numbers, that you have entered: ", number_accumulator)