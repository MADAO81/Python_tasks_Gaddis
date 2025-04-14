# Date printer. Write a program that reads a string value from the user,
# containing a date in the format dd/mm/yyyy. It should print the date in the format  - 12 March 2018


def main():
    # get user input
    usersdate = input("Enter the date in the format dd/mm/yyyy: ")
    conversed_date = date_conversion(usersdate)
    print("Conversed date: ", conversed_date)


def date_conversion(somedate):
    # create local valuables
    day = 0
    month_number = 0
    year = 0
    month_name = ""
    full_date = ""
    # create list of months
    months = ["January", "February", "March",
              "April", "May", "June", "July",
              "August", "September", "October",
              "November", "December"]

    # separate string
    date_list = somedate.split("/")

    # get date,month and year
    day = date_list[0]
    month_number = int(date_list[1])
    year = date_list[2]

    # convert number of month to the name
    month_name = months[month_number - 1]

    # get full date
    full_date = day + " " + month_name + " " + year
    return full_date


main()
