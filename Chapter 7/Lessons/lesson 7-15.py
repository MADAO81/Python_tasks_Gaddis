# this program reads file content to list

def main(): 
    # open file to read
    infile = open("cities.txt", "r")
    
    # read file content to list
    cities = infile.readlines()
    
    # close file 
    infile.close()
    
    # delete "\n" symbol from each element
    index = 0
    while index < len(cities):
        cities[index] = cities[index].rstrip('\n')
        index += 1 
        
        
    # print list content
    print(cities)
    

# call main function
main()
    