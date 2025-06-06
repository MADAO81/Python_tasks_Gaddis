# task 10-06

# Medical expenses

class Procedure:
    def __init__(self, name, date, practitioner, charge):
        self.__name = name 
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge
        
    def set_name(self, name):
        self.__name = name 
        
    def set_date(self, date):
        self.__date = date 
        
    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner
        
    def set_charge(self, charge):
        self.__charge = charge
        
    def get_name(self):
        return self.__name
        
    def get_date(self):
        return self.__date 
        
    def get_practitioner(self):
        return self.__practitioner
        
    def get_charge(self):
        return self.__charge
        
    def __str__(self):
        return "Procedure: " + self.__name + "\nDate: " + self.__date + \
        "\nDoctor's name: " + self.__practitioner + "\nCost: " + \
        format(self.__charge, ",.2f") + "\n"