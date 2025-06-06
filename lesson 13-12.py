# This program demonstrates a group of Radiobutton elements.
import tkinter
import tkinter.messagebox 

class MyGUI:
    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()
        
        # create two frames: one - for Radiobutton elements
        # another for ordinary elements Button 
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # create an IntVar object for use with Radiobutton elements
        self.radio_var = tkinter.IntVar()
        
        # assign a value 1 to an object IntVar
        self.radio_var.ser(1)
        
        # Create Radiobutton elements in the top_frarne frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame, text = "Option 1", variable = self.radio_var, value = 1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text = "Option 2", variable = self.radio_var, value = 2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text = "Option 3", variable = self.radio_var, value = 3)
        
        # pack Radiobutton elements
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        
        # Create "OK" and button "Exit"
        self.ok_button = tkinter.Button(self.bottom_frame, text = "OK", command = self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Exit", command = self.main_window.destroy)
        
        # pack Button elements 
        self.ok_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        
        # pack the frames 
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # start the main loop 
        tkinter.mainloop()
        
    # show_choice method is a function of reverse call for OK button 
    def show_choice(self):
        tkinter.messagebox.showinfo("Select", "Option select" + str(self.radio_var.get()))
        
# Create an instance of MyGUI class 
my_gui = MyGUI()