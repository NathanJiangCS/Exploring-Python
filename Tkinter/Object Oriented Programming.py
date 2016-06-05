import tkinter as tk

LARGE_FONT = ("Verdana", 12)


#Not parameters but inheritance for the class. Not required

class SeaofBTCapp(tk.Tk):
    #Functions inside a class are called methods
    
    #__init__ method is the initialization and will always run when the class is called
    #Passing self is implied but still do it. Args and Kwargs are sometimes represented
    #with just * and ** respectively.
    #Args (shortform for arguments) represents any number of variables.
    #Kwargs are keyword arguments. Most often, they are dictionaries.
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) #Edge of a window
        
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame
        #Sticky is a combination of alignment and stretch. North South East West
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        #This defines new pages
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

app = SeaofBTCapp()
app.mainloop()


        
