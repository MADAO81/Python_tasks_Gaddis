# The sum of the digits in the string. Write a program that asks the user to enter a series
# of single-digit numbers without separators. The program should display the sum of all
# single-digit numbers in a string value. For example, if the user enters 2514, then
# this method should return the value 12, which is the sum of 2, 5, 1, and 4.

def main():
    # Get user's enter
    numbers_line = input("Enter some single digit numbers(without whitespaces):")
    
    # call calculate function
    total = string_calc(numbers_line)
    print("The sum of numbers in your string: ", total)

# create calculate function. this function gets string value and returns sum of all numerals in it.    
def string_calc(users_string):
    # local valuables
    result = 0
    new_list = []
    # iterate through all the characters in the string value
    for i in users_string:
        new_list += i
    # calculate all numbers in new list    
    for i in new_list:
        result += int(i)
    
    # return total
    return result
    
    
main()