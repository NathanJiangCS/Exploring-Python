#Creates a basic window that is empty

import tkinter

class Window(tkinter.Frame):

    def __init__(self, master = None):
        tkinter.Frame.__init__(self, master)

        self.master = master


root = tkinter.Tk()

app = Window(root)
#Initializes and displays it
root.mainloop()
