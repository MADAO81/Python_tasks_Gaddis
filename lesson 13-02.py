# this program shows empty window

import tkinter

class MyGUI:
    def _init_(self):
        # Create an element of main window interface 
        self.main_window = tkinter.Tk()
        
        # enter the main loop tkinter 
        tkinter.mainloop()
        
# create an instance of the class MyGUI
my_gui = MyGUI 
