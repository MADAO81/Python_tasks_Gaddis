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


    # The Truck class represents a pickup truck.
# It is a subclass of the Automobile class.

class Truck(Automobile):
    # The init method accepts arguments for the manufacturer, model, mileage, price, and type of pickup drive.
    
    def __init__(self, make, model, mileage, price, drive_type):
        # Call the init method of the superclass and pass
        # the required arguments. Note that we also pass self as an argument. 
        Automobile.__init__(self, make, model, mileage, price)
        
        # Initialize __drive_type atribute
        self.__drive_type = drive_type 
        
    # The set_drive_type method is a modifier method for the _drive type attribute.
    
    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type
        
    # The get_drive_type method is the recipient method of the _drive_type attribute.
    def get_drive_type(self):
        return self.__drive_type
        
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
        
        # initialize __pass_cap attribute
        self.__pass_cap = pass_cap 
        
    # The set_pass_cap method is a modifier method for the _pass_cap attribute.
    
    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap 
        
    # The get_pass cap method is the recipient method of the _pass cap attribute.
    
    def get_pass_cap(self):
        return self.__pass_cap
        
        

        
        

