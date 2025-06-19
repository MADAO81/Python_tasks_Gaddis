# More than the number "n". In the program, write a function that takes two arguments:
# a list and a number "n". Let's say that the list contains numbers. The function should 
# show all the numbers in the list that are more than "n".

def main():
    # Create list and "n"- number
    some_kind_list = [1, 3, 45, 23, 3.14, 4663, -1000, 43, 6]
    n = 5 
    print("The original list:", some_kind_list)
    print("N-number:",n)
    # passing the list and the number to the function
    print("List of numbers, larger than", n ,"-", comparing_function(some_kind_list,n))
    
    

def comparing_function(some_list, number):
    # create an empty list 
    desired_list = []
    #sort through the numbers in the list and compare them with the "n"-number
    for value in some_list:
        if value > number:
            desired_list.append(value)
    return(desired_list)
    

main()