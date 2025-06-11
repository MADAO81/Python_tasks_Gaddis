# Hollywood star 

import tkinter 

# named constants 
CANVAS_WIDTH = 100 
CANVAS_HEIGHT = 100 
X1 = 50
Y1 = 1
X2 = 20 
Y2 = 91 
X3 = 97
Y3 = 35
X4 = 2 
Y4 = 35 
X5 = 79
Y5 = 91 
TEXT_X = 50
TEXT_Y = 35

class MyGUI:
    def __init__(self):
        # create main window 
        self.main_window = tkinter.Tk()
        
        # create Canvas interface element
        self.canvas = tkinter.Canvas(self.main_window, width =CANVAS_WIDTH, height = CANVAS_HEIGHT)
        
        # draw a star 
        self.canvas.create_text(TEXT_X, TEXT_Y, text = "MADAO", anchor = tkinter.N, fill = "yellow")
        
        # pack the canvas 
        self.canvas.pack()
        
        # start main loop 
        tkinter.mainloop()
        
# create an instance of MyGUI class 
my_gui = MyGUI()