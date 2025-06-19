# task 10-05

# RetailItem class

class RetailItem:
    def __init__(self,decsription, inventory, price):
        self.__description = decsription
        self.__inventory = inventory
        self.__price = price 
        
    def set_description(self, decsription):
        self.__description = decsription
        
    def set_inventory(self, inventory):
        self.__inventory = inventory
        
    def set_price(self, price):
        self.__price = price
        
    def get_description(self):
        return self.__description
        
    def get_inventory(self):
        return self.__inventory
        
    def get_price(self):
        return self.__price
        
    def __str__(self):
        result = "Description: " + self.get_description() + "Units in stock: " + str(self.get_inventory()) + "Price: " + str(self.get_price()) 
        return result
        