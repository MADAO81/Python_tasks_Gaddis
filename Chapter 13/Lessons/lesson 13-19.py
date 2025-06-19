# This program draws a pie chart on the Canvas element.
import tkinter

class MyGUI:
    def __init__(self):
        self.__CANVAS_WIDTH = 320 # canvas width 
        self.__CANVAS_HEIGHT = 240 # canvas height 
        self.__X1 = 60 # left upper coordinate of X rectangle 
        self.__Y1 = 20 # left upper coordinate of Y rectangle 
        self.__X2 = 260 # right bottom coordinate of X rectangle
        self.__Y2 = 220 # right bottom coordinate of Y rectangle 
        self.__PIE1_START = 0 # start angle of sector 1 
        self.__PIE1_WIDTH = 45 # sector 1 length 
        self.__PIE2_START = 45 # start angle of sector 2 
        self.__PIE2_WIDTH = 90 # sector 2 length
        self.__PIE3_START = 135 # start angle of sector 3 
        self.__PIE3_WIDTH = 120 # sector 3 length
        self.__PIE4_START = 255 # start angle of sector 4 
        self.__PIE4_WIDTH = 105 # sector 4 length
        
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create an element of canvas interface 
        self.canvas = tkinter.Canvas(self.main_window, width = self.__CANVAS_WIDTH, height = self.__CANVAS_HEIGHT)
        
        # draw a sector 1
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2, start = self.__PIE1_START, extent = self.__PIE1_WIDTH, fill = "red")
        
        # draw a sector 2 
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2, start = self.__PIE2_START, extent = self.__PIE2_WIDTH, fill = "green")
        
        # draw a sector 3
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2, start = self.__PIE3_START, extent = self.__PIE3_WIDTH, fill = "black")
        
        # draw a sector 4 
        self.canvas.create_arc(self.__X1, self.__Y1, self.__X2, self.__Y2, start = self.__PIE4_START, extent = self.__PIE4_WIDTH, fill = "yellow")
        
        # pack the canvas 
        self.canvas.pack()
        
        # start main loop 
        tkinter.mainloop()
        
# create an instance of MyGUI class
my_gui = MyGUI()
        