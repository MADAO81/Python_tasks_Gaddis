# Property tax

import tkinter
from tkinter.ttk import *

class PropertyGUI:
    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()
        
        # create frames
        self.value_frame = Frame(self.main_window)
        self.assess_frame = Frame(self.main_window)
        self.tax_frame = Frame(self.main_window)
        self.bottom_frame = Frame(self.main_window)
        
        # create an interface elements for value_frame
        self.value_label = Label(self.value_frame, text = "Enter the value of the property: $")
        sefl.value_entry = Entry(self.value_frame, width = 10)
        
        # pack the value_frame elements
       self.value_label.pack(side = "left")
       self.value_entry.pack(side = "left")
       
       # create an interface elements for assess_frame
       self.assess_results_label = Label(self.assess_frame, text = "Estimated value: ")
       
       # create an empty field for estimated value 
       self.assess = tkinter.StringVar()
       self.assess_label = Label(slef.assess_frame, textvariable = self.assess)
       
       # create an interface elements for assess_frame
       self.assess_results_label.pack(side = "left")
       self.assess_label.pack(side = "left")
       
       # create an interface elements for tax_frame 
       self.tax_results_label = Label(self.tsx_frame, text = "Property tax: ")
       
       # create an empty field for value of the property tax 
       self.tax = tkinter.StringVar()
       self.tax_label = Label(self.tax_frame, textvariable = self.tax)
       
       # pack the elements of tax_frame
       self.tax_results_label.pack(side = "left")
       self.tax_label.pack(side = "left")
       
       # create two buttons at the bottom frame 
       self.display_button = Button(self.bottom_frame, text = "Calculate", command = self.calculate)
       self.quit_button = Button(self.bottom_frame, text = "Quit", command = self.main_window.destroy)
       
       # pack the elements at the bottom_frame
       self.display_button.pack(side ="left")
       self.quit_button.pack(side = "left")
       
       # pack the frames 
       self.value_frame.pack()
       self.assess_frame.pack()
       self.tax_frame.pack()
       self.bottom_frame.pack()
       
       # enter the main loop of tkinter
       tkinter.mainloop()
       
       # definite the  show_info function
       def calculate(self):
           # get the entered values 
           self.value = float(self.value_entry.get())
           
           # calculate the assessed value
           self.assessment = 0.60 * self.value 
           
           # update the field with assessed value
           self.assess.set("$" + str(self.assessment))
           
           # calculate the tax 
           self.property_tax = float(self.assessment) / 100 * 0.75 
           
           # update the field with tax 
           self.tax.set("$" + str(self.property_tax))
           
# create an instance of PropertyGUI
prop = PropertyGUI()
       