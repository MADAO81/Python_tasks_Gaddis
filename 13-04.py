# From Celsius to Fahrenheit scale

import tkinter
from tkinter.ttk import 

class CelsiusGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create frames 
        self.top_frame = Frame(self.main_window)
        self.mid_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        
        # create interface elements for upper frame 
        self.celsius_label = Label(self.top_frame, text = "Enter the temperature in degrees Celsius: ")
        self.celsius_entry = Entry(self.top_frame, width = 10)
        
        # pack the upper frame elements
        self.celsius_label.pack(side = "left")
        self.celsius_entry.pack(side = "left")
        
        # create interface elements for middle frame 
        self.results_label = Label(self.mid_frame, text = "Temperature on the Fahrenheit scale: ")
        
        # create an empty field 
        self.fahr = tkinter.StringVar()
        self.fahrenheit_label = Label(self.mid_frame, textvariable = self.fahr)
        
        # pack the middle frame elements
        self.results_label.pack(side = "left")
        self.fahrenheit_label.pack(side = "left")
        
        # create two buttons in the bottom frame 
        self.fahrenheit_button. = Button(self.bottom_frame, text = "Convert to degrees Fahrenheit", command = self.convert)
        self.quit_button = Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)
        
        # pack the elements of bottom frame 
        self.fahrenheit_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        
        # pack the frames 
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        # enter the main loop of tkinter 
        tkinter.mainloop()
        
    # definite the show_info function
    def convert(self):
        # get the entered values 
        self.celsius = float.(self.celsius_entry.get())
        
        # calculate Fahrenheit degrees
        self.fahrenheit = 9.0/5.0*float(self.celsius) + 32
        
        # update fahrenheit_label field 
        self.fahr.set(self.fahrenheit)
        
# create an instance of  CelsiusGUI
celsius =  CelsiusGUI()
        