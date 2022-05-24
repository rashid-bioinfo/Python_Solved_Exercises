from tkinter import *
from Window2_class import *

class Window1:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        self.button1 = Button(self.frame, text="Load Window 2", command=self.loadwindow2)
        self.button1.pack()

    def loadwindow2(self):
        self.newwindow = Toplevel(self.master)
        self.newwindow.geometry('200x150')
        self.app = Window2(self.newwindow)