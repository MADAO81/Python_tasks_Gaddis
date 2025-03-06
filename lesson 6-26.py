# This program shows total amount of sales from file

def main():
    total = 0.0
    try:
        # open file
        infile = open('sales_data.txt', 'r')

        # read data from file and add it to total
        for line in infile:
            amount = float(line)
            total += amount
        # close file
        infile.close()

        # print result
        print(f"{total:.2f}")

    except IOError:
        print("Error while reading file.")

    except ValueError:
        print("There are not numeral data in file.")

    except:
        print("Error!")

# call main function
main()

