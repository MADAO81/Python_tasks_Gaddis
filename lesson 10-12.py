# The CellPhone class contains data about a cell phone

class CellPhone:
    
    # __init__ method initialize the atributes
    
    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price 
        
    # set_manufact method accepts an argument for cellphone manufacturer
    
    def set_manufact(self, manufact):
        self.__manufact = manufact 
        
    # set_model method accepts an argument for phone model number
    
    def set_model(self, model):
        self.__model = model 
        
    # set_retail_price method  accepts an argument for phone retail price 
    
    def set_retail_price(self, price):
        self.__retail_price = price 
        
    # get_manufact method returns phone manufacturer
    def get_manufact(self):
        return self.__manufact
        
    # get_model method returns phone model number
    def get_model(self):
        return self.__model
        
    # get_retail_price method returns phone retail price 
    def get_retail_price(self):
        return self.__retail_price 
        