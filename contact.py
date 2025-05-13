# Contact class contains contact information

class Contact:
    # __init__ method initialize attributes
    def __init__(self, name, phone, email):
        self.__name = name 
        self.__phone = phone
        self.__email = email 
        
    # set_name method sets the attribute "name"
    def set_name(self, name):
        self.__name = name 
        
    # set_phone method sets attribute "phone"
    def set_phone(self, phone):
        self.__phone = phone
        
    # set_email method sets attribute email 
    def set_email(self, email):
        self.__email = email 
        
    # get_name method returns attribute "name"
    def get_name(self):
        return self.__name 
        
    # get_phone method returns attribute "phone"
    def get_phone(self):
        return self.__phone
        
    # get_email method returns attribute email 
    def get_email(self):
        return self.__email
        
    # __str__ method returns the state of the object as a string value
    def __str__(self):
        return "Name: " + self.__name + "Phone: " + self.__phone + "Email: " + self.__email 


