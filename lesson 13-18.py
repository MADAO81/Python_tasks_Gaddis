# This program draws an arc on the Canvas element
import tkinter

class MyGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create interface elemen Canvas
        self.canvas = tkinter.Canvas(self.main_window, width = 200, height = 200)
        
        # draw an arc
        self.canvas.create_arc(10, 10, 190, 190, start = 45, extent = 30)
        
        # pack the canvas 
        self.canvas.pack()
        
        # start main loop
        tkinter.mainloop()
        
# create an instance of MyGUI class 
my_gui = MyGUI()