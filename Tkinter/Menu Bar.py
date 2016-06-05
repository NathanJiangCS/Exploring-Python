#Creates a basic menu bar with drop downs that carry out actions
from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        
        self.pack(fill=BOTH, expand = 1)
        #Defines the menu and where it goes
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        #Adds a quit command to the file button in the menu
        file.add_command(label="Exit", command=self.client_exit)
        #Adss a save command to the file button in the menu
        file.add_command(label="Save")
        #Initializes the file button in the menu
        menu.add_cascade(label="File", menu=file)

        #Adds an undo command to the edit drop down in the menu
        edit = Menu(menu)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)
        
    #Defining the command for the quit button
    def client_exit(self):
        exit()
        
root = Tk()
#Initial Window size
root.geometry("400x300")

app = Window(root)
#Initializes and displays it
root.mainloop()
