# task 13-01
# Name and address 

import tkinter
from tkinter.ttk import

class ShowInfoGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create two frames
        self.top_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        
        # Create an empty field in upper frame 
        self.value = tkinter.StringVar()
        self.address_label = Label(self.top_frame, textvariable=self.value)
        
        # Create two buttons in bottom frame 
        self.address_button = Button(self.bottom_frame, text = "Show info", command = self.show_info)
        self.quit_button = Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)
        
        # pack the Label element 
        self.address_label.pack()
        
        # pack the Button elements 
        self.address_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        
        # pack the Frame elements 
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # Enter the main loop of tkinter
        tkinter.mainloop()
        
    # definite show_info function 
    def show_info(self):
        self.value.set("John Doe\n777 Springfield\n", "Bell, Texas, 55555")
        
# create an instance of ShowInfoGUI class
show_info = ShowInfoGUI()