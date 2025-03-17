# The average number of steps. write a program that reads a file and outputs the average number of steps for each month, 
# for 28 days in February.

def main():

    # open file to read
    steps_file = open("steps.txt","r")
    # make a tuple with months
    mdays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # make a print form 
    print("Month"+"\t\t"+"Average steps")
    # get first date from file 
    date = steps_file.readline()
    start = 0 
    for month in range(len(mdays)):
        end = start + mdays[month]
        steps = readline[begin:end]
    	sum_of_steps = 0 
    	for s in steps: 
        	sum_of_steps = sum_of_steps + int(s)
        
        
    average = sum_of_steps/mdays[m]
    print(str(m+1)+"\t\t"+str(average))
    start = start +mdays[m]

    # close file
    steps_file.close()

# call main
main()