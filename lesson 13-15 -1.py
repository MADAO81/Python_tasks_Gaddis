# This program connects several points with straight line segments.
import tkinter

class MyGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create the Canvas interface element.
        self.canvas = tkinter.Canvas(self.main_window, width = 200, height = 200)
        
        # Draw straight line segments connecting several points.
        points = [10, 10, 189, 10, 100, 189, 10, 10]
        self.canvas.create_line(points)
        
        # pack canvas 
        self.canvas.pack()
        
        # start main loop
        tkinter.mainloop()
        
# create an instance of MyGUI class 
my_gui = MyGUI()