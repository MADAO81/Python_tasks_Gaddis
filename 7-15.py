# Chart of weekly gasoline prices for 1994
import matplotlib.pyplot as plt 
from matplotlib import rcParams
rcParams['font.family']     = 'sans-serif'
rcParams['font.sans-serif'] = ['Ubuntu Condensed']
rcParams['figure.figsize']  = (7, 6)
rcParams['legend.fontsize'] = 10
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9

# named constant
NUM_WEEKS = 52

def main():
    # open file with data
    gas_file = open(r"data\1994_Weekly_Gas_Averages.txt", "r")
    
    # read file content to list
    gas = gas_file.readlines()
    
    # close file 
    gas_file.close()
    
    # cut off new line symbol from every element
    for i in range(len(gas)):
        gas[i] = gas[i].rstrip("\n")
        
    # create list with numbers of weeks (to use 'em as x-coords)
    x_coords = []
    for i in range(1, NUM_WEEKS +1):
        x_coords.append(i)
    
    # build line chart 
    plt.plot(x_coords, gas)
    
    # Limit the X-axis to a range between 1-52
    plt.xlim(xmin=1, xmax=NUM_WEEKS)
    
    # add header
    plt.title("Average weekly gasoline prices in 1994")
    # add marks to axises
    plt.xlabel("Weeks by number")
    plt.ylabel("Average prices")
    
    # show a graph
    plt.show()
        
# call main function
main()