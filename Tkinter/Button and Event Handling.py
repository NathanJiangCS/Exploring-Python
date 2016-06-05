#Creates a basic window with a button
#Includes event handling in order to make the button perform an action
from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        
        self.pack(fill=BOTH, expand = 1)
        
        #Initializing and placing the quit button
        #Command is what the button does
        quitButton = Button(self, text = "Quit", command=self.client_exit)
        quitButton.place(x=0,y=0)
        
    #Defining the command for the quit button
    def client_exit(self):
        exit()
        
root = Tk()
#Initial Window size
root.geometry("400x300")

app = Window(root)
#Initializes and displays it
root.mainloop()
