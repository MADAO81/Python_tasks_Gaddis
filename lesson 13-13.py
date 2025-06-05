# This program demonstrates a group of Checkbutton elements.
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()
        
        # create two frames. one for elements Checkbutton, another for ordinare elements Button 
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create three objects IntVar for use with Checkbutton elements
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        
        # Assign IntVar objects values of 0 
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        
        # Create CheckButton elements in the top_frarne frame.
        self.cb1 = tkinter.CheckButton(self.top_frarne, text = "Option 1", variable = self.cb_var1)
        self.cb2 = tkinter.CheckButton(self.top_frarne, text = "Option 2", variable = self.cb_var2)
        self.cb3 = tkinter.CheckButton(self.top_frarne, text = "Option 3", variable = self.cb_var3)
        
        # pack the elements of CheckButton
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        
        # create "OK" and "Exit" buttons 
        self.ok_button = tkinter.Button(self.bottom_frame, text = "OK", command = self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Exit", command = self.main_window.destroy)
        
        # pack the Button elements 
        self.ok_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        
        # pack the frames
        self.top_frarne.pack()
        self.bottom_frame.pack()
        
        # start main loop 
        tkinter.mainloop()
        
    # show_choice method is function of reverse call for "OK" Button
    
    def show_choice(self):
        # create string value with message 
        self.message = "You selected:\n"
        
        # Determine which Checkbutton elements have been selected and compose an appropriate message.
        if self.cb_var1.get() == 1:
            self.message = self.message + "1\n"
        if self.cb_var2.get() == 1:
            self.message = self.message + "2\n"
        if self.cb_var3.get() == 1:
            self.message = self.message + "3\n"         
        
        # Display the message in the information dialog box.
        tkinter.messagebox.shoinfo("Select", self.message)
        
# create an instance of MyGUI class 
my_gui = MyGUI()
