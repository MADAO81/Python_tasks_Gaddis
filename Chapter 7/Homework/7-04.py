# Number Analysis Program. 
# Design a program that asks the user to enter a series of 20 numbers. 
# The program should store the numbers in a list and then display the data below:
# the smallest number in the list; 
# the largest number in the list; 
# the sum of the numbers in the list; 
# the arithmetic mean of the numbers in the list.

def main():
    # creaty variables
    min_number = 0.0
    max_number = 0.0 
    num_sum = 0.0 
    average = 0.0 
    # create an empty list 
    numbers_list = []
    # add numerals to the list:
    for i in range(20):
        numbers_list.append(float(input("Enter the number:")))
    
    min_number = min(numbers_list)
    max_number = max(numbers_list)
    num_sum = sum(numbers_list)
    average = num_sum / len(numbers_list)
    print("Here is the list of your numbers:", numbers_list)
    print("The minimum number in the list:", min_number)
    print("The maximum number in the list", max_number)
    print("The sum of numbers in your list:", num_sum)
    print("Arithmetic mean of numbers in list:", average)
    
main()