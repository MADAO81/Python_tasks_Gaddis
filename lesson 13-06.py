# This program creates labels in two different frames.

import tkinter

class MyGUI:
    def __init__(self):
        # Create an interface element for the main window.
        self.main_window = tkinter.Tk()
        
        # Create two frames: one for the upper part
        # of the window and the other for the lower part.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create three Label interface elements for the upper frame.
        self.label1 = tkinter.Label(self.top_frame, text = "Blink")
        self.label2 = tkinter.Label(self.top_frame, text = "Wink")
        self.label3 = tkinter.Label(self.top_frame, text = "Nod")
        
        # Pack the labels located in the upper frame. Apply the side argument='top' to
        # place them one below the other.
        self.label1.pack(side = "top")
        self.label2.pack(side = "top")
        self.label3.pack(side = "top")
        
        # Create three Label interface elements for the bottom frame.
        self.label4 = tkinter.Label(self.bottom_frame, text = "Blink")
        self.label5 = tkinter.Label(self.bottom_frame, text = "Wink")
        self.label6 = tkinter.Label(self.bottom_frame, text = "Nod")
        
        # Pack the labels located in the bottom frame. Apply the side='left' argument to
        # position them horizontally to the left of the frame.
        self.label4.pack(side = "left")
        self.label5.pack(side = "left")
        self.label6.pack(side = "left")
        
        # Yes, and we also need to pack the frames!
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # Enter the main loop tkinter
        tkinter.mainloop()
        
# Create an instance of class MyGUI
my_gui = MyGUI()