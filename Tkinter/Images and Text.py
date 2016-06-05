#Continuation from Menu bar
#Displays image and text

from tkinter import *
from PIL import Image, ImageTk
class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        
        self.pack(fill=BOTH, expand = 1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        file.add_command(label="Save")
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        #Add empty parameters from self.showImg and self.showTxt
        #this initializes it immediately
        edit.add_command(label='Show Image', command=self.showImg)
        edit.add_command(label='Show Text', command=self.showTxt)

        menu.add_cascade(label='Edit', menu=edit)
        
    def client_exit(self):
        exit()

    def showImg(self):
        #Image from PIL
        load = Image.open('sampleImage.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

    def showTxt(self):
        text = Label(self, text="Twice x Once")
        text.pack()
        
root = Tk()
#Initial Window size
root.geometry("400x300")

app = Window(root)
#Initializes and displays it
root.mainloop()
