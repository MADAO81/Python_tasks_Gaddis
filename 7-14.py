# pie chart of expenses
import matplotlib.pyplot as plt 
from matplotlib import rcParams
rcParams['font.family']     = 'sans-serif'
rcParams['font.sans-serif'] = ['Ubuntu Condensed']
rcParams['figure.figsize']  = (4, 3.8)
rcParams['legend.fontsize'] = 10
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9

def main():
    # open file with expenses
    expense_file = open(r"data\expenses.txt", "r")
    
    # read file content to list
    expenses = expense_file.readlines()
    
    # close file
    expense_file.close()
    
    # cut off new line symbol from every element
    for i in range(len(expenses)):
        expenses[i] = expenses[i].rstrip("\n")
        
    # creat fraction marks
    slice_labels = ["Rent", "Fuel", "Food", "Clothes", "Car maintenance", "Other"]
    
    # create pie chart from these values
    plt.pie(expenses, labels = slice_labels)
    
    # Add header
    plt.title("Monthly expenses")
    
    # show pie chart
    plt.show()
    
# call main function
main()