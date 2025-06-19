# this program demonstrates the Canvas interface element.
import tkinter

class MyGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create the Canvas interface element.
        self.canvas = tkinter.Canvas(self.main_window, width = 200, height = 200)
        
        # draw two straigt lines 
        self.canvas.create_line(0, 0, 199,199)
        self.canvas.create_line(199, 0, 0, 199)
        
        # pack canvas 
        self.canvas.pack()
        
        # start main loop
        tkinter.mainloop()
        
# create an instance of MyGUI class 
my_gui = MyGUI()