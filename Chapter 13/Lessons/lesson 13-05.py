# This program shows two Label elements with text. and uses argument side = "left"


import tkinter 

class MyGUI:
    def __init__(self): 
        # create an interface element for the  main window 
        self.main_window = tkinter.Tk()
        
        # create first interface element Label that contais record "Hello, world!"
        self.label1 = tkinter.Label(self.main_window, text = "Hello, world!")
        
        # create second  interface element Label that contais record "This is my program contains HUI"
        self.label2 = tkinter.Label(self.main_window, text = "This is my program with GUI.")
        
        # call pack method of interface element Label 
        self.label1.pack(side = "left")
        self.label2.pack(side = "left")
        
        # enter to the main loop tkinter
        tkinter.mainloop()
        
# create an instance class MyGUI
my_gui = MyGUI()
    
        
        
        