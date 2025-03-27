import random
list1 = [1,3,4,6]

def anyfunction(list):
    sum_of_els = 0
    for number in list:
        sum_of_els += number
    return sum_of_els

print(anyfunction(list1))