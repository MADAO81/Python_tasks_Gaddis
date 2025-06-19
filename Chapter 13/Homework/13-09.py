# Age of the tree

import tkinter

# Named constants
CANVAS_WIDTH = 430
CANVAS_HEIGHT = 260

RING1_X1 = 50
RING1_Y1 = 90
RING1_WIDTH = 100
RING1_HEIGHT = 80

RING2_X1 = 40
RING2_Y1 = 70
RING2_WIDTH = 180
RING2_HEIGHT = 120

RING3_X1 = 30
RING3_Y1 = 50
RING3_WIDTH = 260
RING3_HEIGHT = 160

RING4_X1 = 20
RING4_Y1 = 30
RING4_WIDTH = 340
RING4_HEIGHT = 200

RING5_X1 = 10
RING5_Y1 = 10
RING5_WIDTH = 420
RING5_HEIGHT = 240

class MyGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create a Canvas interface element.
        self.canvas = tkinter.Canvas(self.main_window, width=CANVAS_WIDTH,
                                     height=CANVAS_HEIGHT)

        # Draw the first ring.
        self.canvas.create_oval(RING1_X1,  RING1_Y1,
                                RING1_X1 + RING1_WIDTH, RING1_Y1 + RING1_HEIGHT)
        self.canvas.create_text(RING1_X1 + RING1_WIDTH - 10,
                                RING1_Y1 + RING1_HEIGHT - int((RING1_HEIGHT / 2)),
                                text='1 year', anchor=tkinter.E)

        # Draw the second ring.
        self.canvas.create_oval(RING2_X1,  RING2_Y1,
                                RING2_X1 + RING2_WIDTH, RING2_Y1 + RING2_HEIGHT)
        self.canvas.create_text(RING2_X1 + RING2_WIDTH - 10,
                                RING2_Y1 + RING2_HEIGHT - int((RING2_HEIGHT / 2)),
                                text='2 years', anchor=tkinter.E)

        # Draw the third ring.
        self.canvas.create_oval(RING3_X1,  RING3_Y1,
                                RING3_X1 + RING3_WIDTH, RING3_Y1 + RING3_HEIGHT)
        self.canvas.create_text(RING3_X1 + RING3_WIDTH - 10,
                                RING3_Y1 + RING3_HEIGHT - int((RING3_HEIGHT / 2)),
                                text='3 years', anchor=tkinter.E)

        # Draw the fourh ring
        self.canvas.create_oval(RING4_X1,  RING4_Y1,
                                RING4_X1 + RING4_WIDTH, RING4_Y1 + RING4_HEIGHT)
        self.canvas.create_text(RING4_X1 + RING4_WIDTH - 10,
                                RING4_Y1 + RING4_HEIGHT - int((RING4_HEIGHT / 2)),
                                text='4 years', anchor=tkinter.E)

        # Draw the fifth ring.
        self.canvas.create_oval(RING5_X1,  RING5_Y1,
                                RING5_X1 + RING5_WIDTH, RING5_Y1 + RING5_HEIGHT)
        self.canvas.create_text(RING5_X1 + RING5_WIDTH - 10,
                                RING5_Y1 + RING5_HEIGHT - int((RING5_HEIGHT / 2)),
                                text='5 years', anchor=tkinter.E)
        
        # Pack the canvas.
        self.canvas.pack()
        
        # Start the main loop.
        tkinter.mainloop()

#Start the main loop.
my_gui = MyGUI()
