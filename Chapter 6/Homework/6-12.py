# The average number of steps. write a program that reads a file and outputs the
# average number of steps for each month,
# for 28 days in February.

def main():
    # open file to read
    steps_file = open("steps.txt", "r")
    date = steps_file.readline()
    begin = 0
    # make a tuple with months
    mdays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # make a print form
    print("Month" + "\t\t" + "Average steps")

    for m in range(len(mdays)):
        end = begin + mdays[m]
        steps = date[begin:end]
        sumsteps = 0
    for s in steps:

        sumsteps = sumsteps + int(s)

        average = sumsteps / mdays[m]
        print(str(m + 1) + "\t\t" + str(average))
        begin = begin + mdays[m]

    # close file
    steps_file.close()


# call main
main()