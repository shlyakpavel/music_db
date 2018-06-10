from tkinter import Frame, SUNKEN, Label
from db import db_mean
class StatsFrame(Frame):
    def __init__(self, master, DB):
        Frame.__init__(self, master, borderwidth=1, relief=SUNKEN)
        mean_year = db_mean(DB, 'year')
        l = Label(master, text="Mean year: %d" % mean_year)
        l.pack(side="top", fill="both", expand=True)
        