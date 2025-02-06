#Calculating the factorial of a number.

factorial_number = int(input("Enter the number for calculate it's factorial: "))
factorial = 1
factorial_number_for_print = factorial_number
if factorial_number > 0:
    while factorial_number > 1:
        factorial *= factorial_number
        factorial_number -=1
print("Factorial of ",factorial_number_for_print, ":", factorial)