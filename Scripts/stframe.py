from tkinter import Frame, SUNKEN, Label
from db import db_mean
class StatsFrame(Frame):
    def __init__(self, master, DB):
        Frame.__init__(self, master, borderwidth=1, relief=SUNKEN)
        l = Label(master, text="This is window")
        l.pack(side="top", fill="both", expand=True)
        