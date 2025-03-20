# this program read numbers from file to list

def main():
    # open file to read
    infile = open("numberlist.txt", "r")
    
    # read file content to list 
    numbers = infile.readlines()
    
    # close file 
    infile.close()
    
    # convert each element to "int" type 
    index = 0
    while index < len(numbers): 
        numbers[index] = int(numbers[index])
        index += 1
        
    # print list content
    print(numbers)
    
# call main function
main()

