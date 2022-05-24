from tkinter import *

class Window2:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        self.button2 = Button(self.frame, text="click me", command=self.clicker)
        self.button2.pack()

    def clicker(self):
        print("I am being clicked")