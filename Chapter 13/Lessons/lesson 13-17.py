# This program draws two ovals on the Canvas element.
import tkinter

class MyGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create interface elemen Canvas
        self.canvas = tkinter.Canvas(self.main_window, width = 200, height = 200)
        
        # draw two ovals
        self.canvas.create_oval(20, 20, 70, 70)
        self.canvas.create_oval(100, 100, 180, 130)
        
        # pack the canvas 
        self.canvas.pack()
        
        # start main loop
        tkinter.mainloop()
        
# create an instance of MyGUI class 
my_gui = MyGUI()