# this program shows record with text 

import tkinter 

class MyGUI:
    def __init__(self): 
        # create an interface element for the  main window 
        self.main_window = tkinter.Tk()
        
        # create an interface element Label that contais record "Hello, world!"
        self.label = tkinter.Label(self.main_window, text = "Hello, world!")
        
        # call pack method of interface element Label 
        self.label.pack()
        
        # enter to the main loop tkinter
        tkinter.mainloop()
        
# createan instance class MyGUI
my_gui = MyGUI()
    
        
        
        