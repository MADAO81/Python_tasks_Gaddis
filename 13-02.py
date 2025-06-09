# latin translate

import tkinter
from tkinter.ttk import *

class LatinTranslatorGUI:
    # create main window 
    self.main_window = tkinter.Tk()
    
    # create two frames 
    self.top_frame = Frame(self.main_window)
    self.bottom_frame = Frame(self.main_window)
    
    # create an empty field in the upper frame 
    self.value = tkinter.StringVar()
    self.word_label = Label(self.top_frame, textvariable = self.value)
    
    # Create buttons in bottom frame 
    self.sinister_button = Button(self.bottom_frame, text = "sinister", self.show_word1)
    self.dexter_button = Button(self.bottom_frame, text = "dexter", self.show_word2)
    self.medium_button = Button(self.bottom_frame, text = "medium", self.show_word3)
    
    # pack the Label element
    self.word_label.pack()
    
    # pack the Button elements 
    self.sinister_button.pack(side = "left")
    self.dexter_button.pack(side = "left")
    self.medium_button.pack(side = "left")
    
    # pack the Frame elements
    self.top_frame.pack()
    self.bottom_frame.pack()
    
    # enter the main loop tkinter 
    tkinter.mainloop()
    
    # definite show_word function 
    def show_word1(self):
        self.value.set("left")
    def show_word2(self):
        self.value.set("right")
    def show_word3(self):
        self.value.set("middle")
        
# Create an instance LatinTranslatorGUI
latin_translator = LatinTranslatorGUI()