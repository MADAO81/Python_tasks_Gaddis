# The SUV class represents a jeep. 
# It is a subclass of the Autorno Profile class.

class SUV(Automobile):
    # The init method accepts arguments for
    # manufacturer, model, mileage, price 
    # and passenger capacity.
    
    def __init__(self, make, model, mileage, price, pass_cap):
        # Call the init method of the superclass and pass
        # the required arguments. Note that we also pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        
        # initialize __pass_cap atribute 
        self.__pass_cap = pass_cap 
        
    # The set_pass_cap method is a modifier method for the _pass_cap attribute.
    
    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap 
        
    # The get_pass cap method is the recipient method of the _pass cap attribute.
    
    def get_pass_cap(self):
        return self.__pass_cap
        