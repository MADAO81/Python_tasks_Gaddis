class Book:
    # initialize function
    def __init__(self, title, author, pub):
        self.__title = title
        self.__author = author
        self.__pub = pub 
        
    # Modifier methods
    def set_title(self, title):
        self.__title = title
        
    def set_author(self, author):
        self.__author = author
        
    def set_pub(self, pub):
        self.__pub = pub 
        
    # Recipient methods
    def get_title(self):
        return self.__title
        
    def get_author(self):
        return self.__author
        
    def get_pub(self):
        return self.__pub
        
    # __str__ method 
    def __str__(self):
        state_string = ("Name: " + self.__title +"\n"+
                        "Author: "+ self.__author +"\n"+
                        "Publisher: " + self.__pub + "\n")
                        
        return state_string
    