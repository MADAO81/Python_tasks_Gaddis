# The Automobile class contains general information
# about the vehicle in the warehouse.

class Automobile:
    # The init_method method accepts arguments for
    # the manufacturer, model, mileage, and price. 
    # It initializes the data attributes with these values.
    
    def __init__(self, make, model, mileage, price):
        self.__make = make 
        self.__model = model 
        self.__mileage = mileage 
        self.__price = price 
        
    # The following methods are data attribute modifier methods for this class.
    
    def set_make(self, make):
        self.__make = make 
        
    def set_model(self, model):
        self.__model = model 
        
    def set_mileage(self, mileage):
        self.__mileage = mileage 
        
    def set_price(self, price):
        self.__price = price 
    
    # The following methods are methods that receive data attributes of this class.
        
    def get_make(self):
        return self.__make 
        
    def get_model(self):
        return self.__model 
        
    def get_mileage(self):
        return self.__mileage
        
    def get_price(self):
        return self.__price 
        
    