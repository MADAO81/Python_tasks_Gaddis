repeat_operation = 'yes'
while repeat_operation == 'yes':
    users_value_one = int(input("Enter the first number: "))
    users_value_two = int(input("Enter the second number: "))
    sum_of_values = users_value_one + users_value_two
    print("Sum of your nums is: ", sum_of_values)
    print("Do you want another calculation? yes/no")
    repeat_operation = input()