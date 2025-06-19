# This program converts distances in kilometers to miles. 
# The result is displayed in the Label element in the main window.

import tkinter

class KiloConverterGUI:
    def __init__(self):
        
        # Create main window 
        self.main_window = tkinter.Tk()
        
        # Create three frames for groupping elements of interface
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create interface elements for upper frame 
        self.prompt_label = tkinter.Label(self.top_frame, text = "Enter the distance in kilometers: ")
        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)
        
        # Pack the elements of upper frame 
        self.prompt_label.pack(side="left")
        self.kilo_entry.pack(side = "left")
        
        # Create interface elements for middle frame 
        self.descr_label = tkinter.Label(self.mid_frame, text = "Converted to miles: ")
       
       # The StringVar object is needed in order to associate it with the output label. 
       # To save the sequence of spaces, the set method of this object is used.
        self.value = tkinter.StringVar()
        
        # Create a Label and link it to an object 
        # StringVar. Any values stored in the StringVar object will be automatically output in the Label label.
        self.miles_label = tkinter.Label(self.mid_frame, textvariable = self.value)
        
        # Create an interface elements for middle frame 
        self.descr_label.pack(side="left")
        self.miles_label.pack(side="left")
        
        
        
        # Create elements interface Button for bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text = "Convert!", command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Exit", command = self.main_window.destroy)
        
        # pack the buttons 
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        # pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        # enter the main loop of tkinter
        tkinter.mainloop()
    
    # The convert method is a callback function for the 'Convert' button.
    def convert(self):
        # get the value entered by the user in the interface element kilo_entry
        kilo = float(self.kilo_entry.get())
        
        # convert kilometers to miles 
        miles = kilo * 0.624
        
        # convert miles to a string value and save it in a StringVar object. 
        # As a result, the miles_label interface element will be updated automatically.
        self.value.set(miles)
        
# create an instance of class KiloConverterGUI
kilo_conv = KiloConverterGUI()
        