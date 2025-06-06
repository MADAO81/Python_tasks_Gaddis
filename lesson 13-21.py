# This program applies text to the Canvas element.
import tkinter 

class MyGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create an element of Canvas interface
        self.canvas = tkinter.Canvas(self.main_window, width = 160, height = 160)
        
        # show the text in center of window 
        self.canvas.create_text(100, 100, text = "Hello, world!")
        
        # pack the canvas 
        self.canvas.pack()
        
        # start main loop 
        tkinter.mainloop()
        
# create an instance of MyGUI class 
my_gui = MyGUI()