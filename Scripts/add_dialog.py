from tkinter import Frame, SUNKEN, Label

class InsertionFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, borderwidth=1, relief=SUNKEN)
        l = Label(master, text="This is window")
        l.pack(side="top", fill="both", expand=True)
        