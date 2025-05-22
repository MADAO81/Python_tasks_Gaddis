# CashRegister 

import retail

class CashRegister:
    # initialize empty dictionary for purchased goods 
    def __init__(self):
        
        self.__items = []
        
    # Cleans the contents of the cash register.
    def clear(self):
        
        self.__items = []
        
    # Simulates adding an item to the cash register. Gets the Retail Item object as an argument.
    def purchase_item(self, retail_item):
        
        self.__items.append(retail_item)
        print("The product was added to the cash register.")
        
    # Returns the total cost of the items at the cash register.
    def get_total(self):
        
        total = 0.0
        for item in self.__items:
            total = total + item.get_price()
            
        return total 
        
    # Prints the list of products in the cash register.
    def show_items(self):
        
        print("Products at the cash register: ")
        print()
        for item in self.__items:
            print(item)
            print()
        