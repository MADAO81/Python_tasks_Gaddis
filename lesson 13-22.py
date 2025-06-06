# This program applies text to the Canvas element.
import tkinter 

class MyGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create an element of Canvas interface
        self.canvas = tkinter.Canvas(self.main_window, width = 500, height = 200)
        
        # create a Font object
        myfont = tkinter.font.Font(family="Helvetica", size=18, weight="bold")
        
        # show the text in center of window 
        self.canvas.create_text(100, 100, text = "Hello, world!", font=myfont)
        
        # pack the canvas 
        self.canvas.pack()
        
        # start main loop 
        tkinter.mainloop()
        
# create an instance of MyGUI class 
my_gui = MyGUI()