# this program contains "Exit" button 

import tkinter 
import tkinter.messagebox 

class MyGUI:
    def __init__(self):
        # Create an interface element for the main window.
        self.main_window = tkinter.Tk()
        
        # Create a Button widget interface element. The text 'Click me!' should appear on the button. 
        # When the user clicks the button, the do_something method should be executed.
        self.my_button = tkinter.Button(self.main_window, text = "Push me!", command = self.do_something)
        
        # Create an Exit button. When this button is clicked, 
        # the destroy method of the root interface element is called 
        # (the main_window variable refers to the root element, sothe callback function is self.main_window.destroy.)
        self.quit_button = tkinter.Button(self.main_window, text = "Exit", command = self.main_window.destroy)
        
        # Pack the Button interface elements.
        self.my_button.pack()
        self.quit_button.pack()
        
        # Enter to main loop tkinter
        tkinter.mainloop()
        
    # The do something method is a callback function for the Button interface element.
    def do_something(self):
        # Show info dialog window 
        tkinter.messagebox.showinfo("Reaction", "Praise you for push the button!")
        
# create an instance of MyGUI class 
my_gui = MyGUI()