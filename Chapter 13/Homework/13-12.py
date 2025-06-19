# The solar system 

import tkinter

# Named constants
CANVAS_WIDTH = 520
CANVAS_HEIGHT = 300
SPACING = 10

SUN_X = 60
SUN_Y = 150
SUN_RAD = 50
SUN_COLOR = 'yellow'

MERC_RAD = 10
MERC_X = SUN_X + SUN_RAD + SPACING + MERC_RAD
MERC_Y = 150
MERC_COLOR = 'orange'

VENUS_RAD = 15
VENUS_X = MERC_X + MERC_RAD + SPACING + VENUS_RAD
VENUS_Y = 150
VENUS_COLOR = 'lightblue'

EARTH_RAD = 10
EARTH_X = VENUS_X + VENUS_RAD + SPACING + EARTH_RAD
EARTH_Y = 150
EARTH_COLOR = 'blue'

MARS_RAD = 8
MARS_X = EARTH_X + EARTH_RAD + SPACING + MARS_RAD
MARS_Y = 150
MARS_COLOR = 'red'

JUPITER_RAD = 30
JUPITER_X = MARS_X + MARS_RAD + SPACING + JUPITER_RAD
JUPITER_Y = 150
JUPITER_COLOR = 'brown'

SAT_RAD = 30
SAT_X = JUPITER_X + JUPITER_RAD + SPACING + SAT_RAD
SAT_Y = 150
SAT_COLOR = 'blanched almond'

URN_RAD = 20
URN_X = SAT_X + SAT_RAD + SPACING + URN_RAD
URN_Y = 150
URN_COLOR = 'deep sky blue'

NEP_RAD = 17
NEP_X = URN_X + URN_RAD + SPACING + NEP_RAD
NEP_Y = 150
NEP_COLOR = 'light steel blue'

PLU_RAD = 5
PLU_X = NEP_X + NEP_RAD + SPACING + PLU_RAD
PLU_Y = 150
PLU_COLOR = 'dark olive green'

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create a Canvas interface element.
        self.canvas = tkinter.Canvas(self.main_window,
                                     width=CANVAS_WIDTH,
                                     height=CANVAS_HEIGHT)
        # Draw planets
        self.draw_planet(self.canvas, SUN_X, SUN_Y, SUN_RAD, SUN_COLOR, 'Sun')
        self.draw_planet(self.canvas, MERC_X, MERC_Y, MERC_RAD, MERC_COLOR, 'Mercury')
        self.draw_planet(self.canvas, VENUS_X, VENUS_Y, VENUS_RAD, VENUS_COLOR, 'Venus')
        self.draw_planet(self.canvas, EARTH_X, EARTH_Y, EARTH_RAD, EARTH_COLOR, 'Earth')
        self.draw_planet(self.canvas, MARS_X, MARS_Y, MARS_RAD, MARS_COLOR, 'Mars')
        self.draw_planet(self.canvas, JUPITER_X, JUPITER_Y, JUPITER_RAD, JUPITER_COLOR, 'Jupiter')
        self.draw_ringed_planet(self.canvas, SAT_X, SAT_Y, SAT_RAD, SAT_COLOR, 'Saturn')
        self.draw_planet(self.canvas, URN_X, URN_Y, URN_RAD, URN_COLOR, 'Uranus')
        self.draw_planet(self.canvas, NEP_X, NEP_Y, NEP_RAD, NEP_COLOR, 'Neptune')
        self.draw_planet(self.canvas, PLU_X, PLU_Y, PLU_RAD, PLU_COLOR, 'Pluto')

        # Pack the canvas.
        self.canvas.pack()
        
        # Start the main loop.
        tkinter.mainloop()

    # The draw_planet method draws a circle with a center
    # point in x,y on the canvas. The radius parameter sets 
    # the radius of the circle and the color parameter sets the color of the circle fill.
    def draw_planet(self, canvas, x, y, radius, color, name):
        x1 = int(x) - int(radius)
        y1 = int(y) - int(radius)
        x2 = int(x) + int(radius)
        y2 = int(y) + int(radius)
        canvas.create_oval(x1, y1, x2, y2, fill=color)
        canvas.create_text(x, y2, text=name, anchor=tkinter.N)

    # The draw_ringed_planet method draws a ringed planetу.
    def draw_ringed_planet(self, canvas, x, y, radius, color, name):
        # Draw a ring.
        ring_x1 = int(x) - int(radius) - SPACING
        ring_y1 = int(y) - int(radius) + SPACING
        ring_x2 = int(x) + int(radius) + SPACING
        ring_y2 = int(y) + int(radius) - SPACING
        canvas.create_oval(ring_x1, ring_y1, ring_x2, ring_y2)
        
        # Draw a planet.
        self.draw_planet(canvas, x, y, radius, color, name)
        
# Create an instance of the MyGUI class.
my_gui = MyGUI()