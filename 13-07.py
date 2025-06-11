# Long-distance calls

import tkinter
from tkinter.ttk import *
import tkinter.messagebox

class AutoGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create frames 
        self.top_frame = Frame(self.main_window)
        self.mid_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        
        # create  valuable for use with radiobuttons 
        self.rb_var = tkinter.IntVar()
        
        # Assign a variable 1
        self.rb_var.set(1)
        
        # Create Radiobutton elements in the upper frame
        self.rb1 = Radiobutton(self.top_frame, text = "Day time (6:00 - 17:59)", variable = self.rb_var, value = 1)
        self.rb2 = Radiobutton(self.top_frame, text = "Evening time (18:00 - 23:59)", variable = self.rb_var, value = 2)
        self.rb3 = Radiobutton(self.top_frame, text ="Off-peak period (00:00 - 5:59)", variable = self.rb_var, value = 3)
        
        # pack the Radiobutton elements
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        
        # Create interface elements for the middle frame
        self.minutes_label = Label(self.mid_frame, text = "Enter the number of minutes: ")
        self.minutes.entry = Entry(self.mid_frame, width = 10)
        
        # Pack the elements in a value_frame 
        self.minutes_label.pack(side = "left")
        self.minutes_entry.pack(side = "left")
        
        # Create two buttons at the bottom frame 
        self.display_button = Button(self.bottom_frame, text = "Show cost", command = self.calculate)
        self.quit_button = Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)
        
        # pack the elements at the bottom frame
        self.display_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        
        # pack the frames 
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        # enter the main loop of tkinter
        tkinter.mainloop()
        
    # definite calculate function
    def calculate(self):
        # Get the entered value
        self.minutes = float(self.minutes_entry.get())
        
        # Determine the tariff based on the selected radio button
        if self.rb_var.get() == 1:
            self.rate = 0.07 
        if self.rb_var.get() == 2:
            self.rate = 0.12 
        if self.rb_var.get() == 3:
            self.rate = 0.05
            
        # calculate cost
        self.charges = self.minutes * self.rate 
        
        # show the information window
        tkinter.messagebox.showinfo("Total cost", "Your costs = $" + format(self.charges, ",.2f"))
        
# create an istance of LongDistanceGUI
long_dist = LongDistanceGUI()
     