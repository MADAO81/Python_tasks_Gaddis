# The Truck class represents a pickup truck. 
# It is a subclass of the Automobile class.

class Truck(Automobile):
    # The init method accepts arguments for the manufacturer, model, mileage, price, and type of pickup drive.
    
    def __init__(self, make, model, mileage, price, driv_type):
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