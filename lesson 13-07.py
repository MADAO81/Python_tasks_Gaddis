# This program demonstrates the Button interface element.
# When the user clicks the Button, an information dialog box is displayed on the screen.

import tkinter
import tkinter.messagebox 

class MyGUI:
    def __init__(self):
        # Create an interface element for the main window.
        self.main_window = tkinter.Tk()
        
        # Create a Button widget interface element. 
        # The text 'Click me!' should appear on the button.
        # When the user clicks the button,
        # the do_something method should be executed.
        self.my_button = tkinter.Button(self.main_window, text = "Click me!", command = self.do_something)
        
        # Package the Button interface element.
        self.my_button.pack()
        
        # Enter the main tkinter loop.
        tkinter.mainloop()
        
    # The do something method is a callback function for the Button interface element.
    def do_something(self):
        # Show the information dialog box
        tkinter.messagebox.showinfo("Reaction", "Praise you for push the button!")
        
# Create an instance of MyGUI class 
my_gui = MyGUI()