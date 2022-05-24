# Import Tk module
from tkinter import *

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

    

class Window2:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        self.button2 = Button(self.frame, text="click me", command=self.clicker)
        self.button2.pack()

    def clicker(self):
        print("I am being clicked")


# Run program on a continuous loop
root = Tk()
root.geometry("100x100")
app = Window1(root)
root.mainloop()

