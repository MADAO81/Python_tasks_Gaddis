# This program converts the distance in kilometers to miles. 
# The result is displayed in the information dialog box.

import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        
        # Create main window 
        self.main_window = tkinter.Tk()
        
        # Create two frames for groupping elements of interface
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create interface elements for upper frame 
        self.prompt_label = tkinter.Label(self.top_frame, text = "Enter the distance in kilometers: ")
        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)
        
        # Pack the elements of upper frame 
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side = "left")
        
        # Create elements interface Button for upper frame
        self.calc_button = tkinter.Button(self.bottom_frame, text = "Convert!", command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Exit", command = self.main_window.destroy)
        
        # pack the buttons 
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # enter the main loop of tkinter
        tkinter.mainloop()
        
    # The convert method is a callback function for the 'Convert' button.
    
    def convert(self):
        # Get the value entered by the user in the kilo_entry interface element.
        kilo = float(self.kilo_entry.get())
        
        # convert kilometers to miles 
        miles = kilo * 0.6214
        
        # show result in the information dialog window 
        tkinter.messagebox.showinfo("Result", str(kilo) + "kilometers is equivalent to ", str(miles) + "miles")
        
# create an instance of class KiloConverterGUI
kilo_conv = KiloConverterGUI()
        
        