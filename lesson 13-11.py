# This program uses a GUI to get three grades and output the average score.

import tkinter

class TestAvg:
    def __init__(self):
        # create main window
        self.main_window = tkinter.Tk()
        
        # create 5 frames 
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        
        # create and pack interface elements for grade 1 
        self.test1_label = tkinter.Label(self.test1_frame, text = "Enter the grade #1: ")
        self.test1_entry = tkinter.Entry(self.test1_frame, width = 10)
        self.test1_label.pack(side = "left")
        self.test1_entry.pack(side = "left")
        
        # create and pack interface elements for grade 2 
        self.test2_label = tkinter.Label(self.test1_frame, text = "Enter the grade #2: ")
        self.test2_entry = tkinter.Entry(self.test1_frame, width = 10)
        self.test2_label.pack(side = "left")
        self.test2_entry.pack(side = "left")
        
        # create and pack interface elements for grade 3 
        self.test3_label = tkinter.Label(self.test1_frame, text = "Enter the grade #3: ")
        self.test3_entry = tkinter.Entry(self.test1_frame, width = 10)
        self.test3_label.pack(side = "left")
        self.test3_entry.pack(side = "left")
        
        # Create and pack interface elements for the average score.
        self.result_label = tkinter.Label(self.avg_frame, text = "Average grade: ")
        self.avg = tkinter.StringVar() # For update avg_label 
        self.avg_label = tkinter.Label(self.avg_frame, textvariable = self.avg)
        self.result_label.pack(side = "left")
        self.avg_label.pack(side = "left")
        
        # Create and pack interface elements for Button 
        self.calc_button = tkinter.Button(self.button_frame, text = "Average", command = self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame, text = "Exit", command = self.main_window.destroy)
        self.calc_button.pack(side = "left")
        self.quit_button.pacl(side = "left")
        
        # pack the frames 
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()
        
        # start main loop 
        tkinter.mainloop()
        
    # The calc_avg method is a callback function for the calc_button interface element.
    
    def calc_avg(self):
        # Get 3 grades and save them to valuables
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())
        
        # calculate the average grade 
        self.average = (self.test1 + self.test2 + self.test3) / 3.0
        
        # update interface element avg_label and save self.average value to the StringVar object
        self.avg.set(self.average)
        
# create an instance of TestAvg class 
test_avg = TestAvg()