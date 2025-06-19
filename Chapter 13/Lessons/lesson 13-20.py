# this program draws a polygon on a Canvas element
import tkinter 

class MyGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create an element of Canvas interface
        self.canvas = tkinter.Canvas(self.main_window, width = 160, height = 160)
        
        # draw a polygon
        self.canvas.create_polygon(60, 20, 100, 20, 140, 60, 140, 100, 100, 140, 60, 140, 20, 100, 20, 60)
        
        # pack the canvas 
        self.canvas.pack()
        
        # start main loop 
        tkinter.mainloop()
        
# create an instance of MyGUI class 
my_gui = MyGUI()