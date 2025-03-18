# The NUM_DAYS constant contains the number of days
# for which we will collect sales data.
NUM_DAYS = 5

def main():
     # Create list, which will contains 
     # the sales for every days
     sales = [0] * NUM_DAYS
     
     # Create value, which will contains the index
     index = 0
     
     print("Enter the sales for every day: ")
     
     # Get sales for every day 
     while index < NUM_DAYS:
         print("Day #", index + 1, ":", sep="", end="")
         sales[index] = float(input())
         index +=1 
     
     # Show entered values
     print("Here is the values, that you have entered: ")    
     for value in sales:
         print(value)
        

# call main function
main()