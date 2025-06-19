# This program demonstrates "split" method by using "/" as divider

def main():
    # create string value with date
    date_string = "09/05/1945"
    
    # split string value
    date_list = date_string.split("/")
    
    # print result
    print("Day:", date_list[0])
    print("Month:", date_list[1])
    print("Year:", date_list[2])
    
# call main function
main()