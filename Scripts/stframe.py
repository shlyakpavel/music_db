from tkinter import Frame, SUNKEN, Label, Button, TOP, BOTH
from db import db_mean
class StatsFrame(Frame):
    data = []
    def __init__(self, master, DB):
        self.database = DB
        Frame.__init__(self, master, borderwidth=1, relief=SUNKEN)
        mean_year = "Mean year: %d" % db_mean(DB, 'year')
        self.mean_year_label = Label(master, text=mean_year)
        self.data.append(mean_year)
        self.mean_year_label.pack(side="top", fill="both", expand=True)
        self.save_btn = Button(master, text="Save", command=self.save)
        self.save_btn.pack(side=TOP, fill=BOTH, expand=True)
        
    def save(self):
        filename=hash(str(self.database)) 
        path = "../Data/" + str(filename) + ".txt"
        file = open(path, "w")
        file.writelines(self.data)