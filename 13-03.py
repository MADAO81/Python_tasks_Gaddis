# Miles per Gallon of Gasoline Calculator

import tkinter
from tkinter.ttk import *

class MilesGUI:
    def __init__(self):
        # Create main window 
        self.main_window = tkinter.Tk()
        
        # create four frames 
        self.gallons_frame = Frame(self.main_window)
        self.miles_frame = Frame(self.main_window)
        self.mpg_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        
        # create interface elements for gallons_frame
        self.gallons_label = Label(self.gallons_frame, text = "Enter the number of gallons:")
        self.gallons_entry = Entry(self.gallons_frame, width = 10)
        
        # pack the elements of gallons_frame
        self.gallons_label.pack(side = "left")
        self.gallons_entry.pack(side = "left")
        
        # create the elements of miles_frame
        self.miles_label = Label(self.miles_frame, text = "Enter the number of miles: ")
        self.miles_entry = Entry(self.miles_frame, width = 10)
        
        # pack the elements of miles_frame 
        self.miles_label.pack(side = "left")
        self.miles_entry.pack(side = "left")
        
        # create interface elements for result_label
        self.result_label = Label(self.mpg_frame, text = "Miles per gallon(MPG) = ")
        
        # create an empty field
        self.mpg = tkinter.StringVar()
        self.mpg_label = Label(self.mpg_frame, textvariable = self.mpg)
        # pack the elements for frame 
        self.result_label.pack(side = "left")
        self.mpg_label.pack(side = "left")
        
        # creater two buttons in the bottom frame 
        self.mpg_button = Button(self.bottom_frame, text = "Calculate MPG", command = self.calculate_mpg)
        self.quit_button = Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)
        
        # pack the interface elements in bottom frame 
        self.mpg_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        
        # pack the frames 
        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.mpg_frame.pack()
        self.bottom_frame.pack()
        
        # enter the main loop of tkinter
        tkinter.mainloop()
        
    # definite the show_info function
    def calculate_mpg(self):
        # get entered values 
        self.gallons = float(self.gallons_entry.get())
        self.miles = float(self.miles_entry.get())
        
        # calculate mpg 
        self.miles_per_gallon = float(self.miles) / self.gallons 
        
        # update mpg_label field 
        self.mpg.set(self.miles_per_gallon)
        
# create an instance of MilesGUI
mpg = MilesGUI()
        
        
        
        