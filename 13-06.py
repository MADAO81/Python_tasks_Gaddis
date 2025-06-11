# car repair company

import tkinter
from tkinter.ttk import *
import tkinter.messagebox

class AutoGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create frames 
        self.top_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        
        # Create variables for use with Checkbuttons elements
        self.cb_oil_var = tkinter.IntVar()
        self.cb_lube_var = tkinter.IntVar()
        self.cb_radiator_var = tkinter.IntVar()
        self.cb_trans_var = tkinter.IntVar()
        self.cb_inspection_var = tkinter.IntVar()
        self.cb_muffler_var = tkinter.IntVar()
        self.cb_tire_var = tkinter.IntVar()
        
        # Assign a value of 0 to variables
        self.cb_oil_var.set(0)
        self.cb_lube_var.set(0)
        self.cb_radiator_var.set(0)
        self.cb_trans_var.set(0)
        self.cb_inspection_var.set(0)
        self.cb_muffler_var.set(0)
        self.cb_tire_var.set(0)
        
        # create flag buttons Checkbutton in the upper frame 
        self.cb1 = Chekbutton(self.top_frame, text = "Change oil - $30.00", variable = self.cb_oil_var)
        self.cb2 = Chekbutton(self.top_frame, text = "Lubricate works - $20.00", variable = self.cb_lube_var)
        self.cb3 = Chekbutton(self.top_frame, text = "Radiator flushing - $40.00", variable = self.cb_radiator_var)
        self.cb4 = Chekbutton(self.top_frame, text = "Replacement of transmission fluid - $100.00", variable = self.cb_trans_var)
        self.cb5 = Chekbutton(self.top_frame, text = "Inspection - $35.00", variable = self.cb_inspection_var)
        self.cb6 = Chekbutton(self.top_frame, text = "Replacing the exhaust muffler - #200.00", variable = self.cb_muffler_var)
        self.cb7 = Chekbutton(self.top_frame, text = "Change tires = $20.00", variable = self.cb_tire_var)
        
        # pack the Chekbutton elements
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        
        # create two buttons at the bottom frame 
        self.display_button = Button(self.bottom_frame, text = "Show the total cost", command = self.calculate)
        self.quit_button = Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)
        
        # pack the elements at the bottom frame 
        self.display_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        
        # pack the frames 
        self.top_frame.pack
        self.bottom_frame.pack
        
        # enter the main loop of tkinter
        tkinter.mainloop()
        
    # definite the show_info function
    def calculate(self):
        # create valuable for total sum 
        self.total = 0.0 
        
        # Determine the total cost based on the selected flag buttons
        if self.cb_oil_var.get() == 1:
            self.total += 30.0
        if self.cb_lube_var.get() == 1:
            self.total += 20.0 
        if self.cb_radiator_var.get() == 1:
            self.total += 40.0 
        if self.cb_trans_var.get() == 1:
            self.total += 100.0 
        if self.cb_inspection_var.get() == 1:
            self.total += 35.0 
        if self.cb_muffler_var.get() == 1:
            self.total += 200.0 
        if self.cb_tire_var.get() == 1:
            self.total += 20.0 
            
        # Show the information window
        tkinter.messagebox.showinfo("Total cost", "Your costs = $" + format(self.total, ",.2f"))
        
# create an instance of AutoGUI
auto = AutoGUI()