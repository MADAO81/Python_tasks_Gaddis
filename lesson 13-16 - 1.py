# This program draws a rectangle on the Canvas element.
import tkinter

class MyGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create the Canvas interface element.
        self.canvas = tkinter.Canvas(self.main_window, width = 200, height = 200)
        
        # Draw rectangle 
        self.canvas.create_rectangle(20, 20, 180, 180, dash = (5, 2), width = 3)
        
        # pack canvas 
        self.canvas.pack()
        
        # start main loop
        tkinter.mainloop()
        
# create an instance of MyGUI class 
my_gui = MyGUI()