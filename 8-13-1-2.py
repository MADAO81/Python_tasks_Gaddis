# PowerBall lottery

# The prevalence of numbers

# Global constant
LOTTERY_NUMBERS = 69

# The get_all_numbers function returns a list with lottery numbers 
# in the file pbnumbers.txt The numbers appear in the order in which they were read from the file.
def get_all_numbers():
    # open file with lottery numbers
    pblottery_file = open(r"data\pbnumbers.txt", "r")
    
    # Read file content to the list
    pblottery = pblottery_file.readlines()
    
    # close file 
    
    # delete from every element new line symbol
    for i in range(len(pblottery)):
        pblottery[i] = pblottery[i].rstrip("\n")
        
        
    # Split each element into separate numbers and save the individual regular numbers in a list called lotto_nums
    lotto_nums = []
    for i in range(len(pblottery)):
        number_set = pblottery[i].split()
        for j in range(len(number_set)):
            lotto_nums.append(int(number_set[j]))
            
    # return list lotto_nums
    return lotto_nums
    
# The get_frequency function takes a list of numbers and determines the frequency of each value in the list. 
# The max_value parameter indicates the maximum value stored in the list.
def get_frequency(number_list, max_value):
    # Create list for every number frequency. every element initializes by 0
    frequency = [0] * (max_value + 1)
    for i in range(len(number_list)):
        # get next lottery number in list 
        num = number_list[i]
        
        # enlarge frequency of this number
        frequency[num] += 1
    
    # return frequency list    
    return frequency

# The position_of_highest_value function returns the position of the largest value in the num_list.
def position_of_highest_value(num_list):
    highest = 0
    highest_position = 0
    for i in range(len(num_list)):
        if num_list[i] > highest:
            highest = num_list[i]
            highest_position = i 
            
    return highest_position
    
# The most_common function takes a freq_list frequency list and returns
# another list in which element 0 contains the position of the largest 
# value in the freq_list list, element 1 contains the position of the second
# largest value in the freq_list list, etc.
def most_common(freq_list):
    # create an empty list for most common values
    common_sorted = []
    
    # create copy of freq_list
    temp_list = []
    for item in freq_list:
        temp_list.append(item)
        
    for i in range(len(temp_list)):
        position = position_of_highest_value(temp_list)
        common_sorted.append(position)
        temp_list[position] = -1 
        
    # return common_sorted list 
    return common_sorted

def main():
    # get list of all lottery numbers 
    lotto_nums = get_all_numbers()
    
    # get frequency for every number
    frequency = get_frequency(lotto_nums, LOTTERY_NUMBERS)
    
    # get list for most common values
    sorted_by_most_common = most_common(frequency)
    
    # show 10 most common numbers 
    print("10 most common numbers(in descending order): ")
    print("--------------------------------------------")
    for i in range(10):
        print(sorted_by_most_common[i])
    
    # show 10 least common numbers
    sorted_by_most_common.reverse()
    print("\n10 most common numbers(in ascending order): ")
    print("--------------------------------------------")
    for i in range(1,11):
        print(sorted_by_most_common[i])
        
# call main function
main()






        