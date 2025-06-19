# Fuel prices

#  Global constants
STARTING_YEAR = 1993
ENDING_YEAR = 2013

def get_price(str):
    items = str.split(":")
    return float(items[1])
    
    
def get_month(str):
    items = str.split("-")
    return int(items[0])
    

def get_day(str):
    items = str.split("-")
    return int(items[1])
    
    
def get_year(str):
    items = str.split("-")
    date_items = items[0].split("-")
    return int(date_items[2])
    

def get_yearly_average(gas_list, year):
    total = 0
    count = 0 
    
    for e in gas_list:
        if get_year(e) == year:
            total += get_price(e)
            count +=1 
            
    average = total / count
    
    return average
    
def main():
    gas_file = open(r"data\GasPrices.txt","r")
    
    gas_list = gas_file.readlines()
    
    for i in range(STARTING_YEAR, ENDING_YEAR + 1):
        prices("Average price in ", i, "is $", format(get_yearly_average(gas_list, i), ".2f"), sep = "")
        
main()