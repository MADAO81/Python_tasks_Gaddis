# Counter of even/odd numbers.
# Write a program that generates 100 random numbers and counts 
# the number of even and odd random numbers
import random

even_counter = 0 
odd_counter = 0
even_list =[]
odd_list = []
random_num_array = [random.randint(1,10000) for i in range(100)] # Create array with 100 random numbers in the interval 0-10000

def even_odd(number):
    if number % 2 == 0:
        status = True
    else:
        status = False
    return status

for num in random_num_array:
    if even_odd(num):
        even_counter += 1
        even_list += [num]
    else:
        odd_counter += 1
        odd_list += [num] 
        
 
print(f"Random numbers: {random_num_array}")
print(f"Even numbers quantity: {even_counter}.")
print(f"Even numbers list:{even_list}")
print(f"Odd numbers quantity: {odd_counter}.")
print(f"Odd numbers list: {odd_list}")


    
