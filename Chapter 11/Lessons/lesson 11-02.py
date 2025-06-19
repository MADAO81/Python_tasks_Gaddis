# The Car class represents a passenger car. It is a subclass of the Automobile class.

class Car(Automobile):
    # The init method accepts arguments for the manufacturer, model, mileage, price, and number of doors.
    
    def __init__(self, make, model, mileage, price, doors):
        # Call the init method of the superclass and pass
        # the required arguments. Note that we also pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        
        # initialize __doors atribute 
        self.__doors = doors 
        
    # The set doors method is a modifier method for the doors attribute.
    
    def set_doors(self, doors):
        self.__doors = doors 
        
    # The get_doors method is the receiving method of the doors attribute.
    
    def get_doors(self):
        return self.__doors 