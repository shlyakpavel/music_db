from tkinter import Frame, SUNKEN, Label, Button, TOP, BOTH
from db import db_mean, db_max, db_min
class StatsFrame(Frame):
    """A simple class to manage statistic (show and save to disk)
    Author: Pavel"""
    data = []
    def __init__(self, master, DB):
        """Class constructor
        Args:
            master - parent widget
            DB - database
        Author: Pavel"""
        self.database = DB
        Frame.__init__(self, master, borderwidth=1, relief=SUNKEN)
        
        mean_year = "Mean year: %d" % db_mean(DB, 'year')
        self.mean_year_label = Label(master, text=mean_year)
        self.data.append(mean_year)
        self.mean_year_label.pack(side=TOP, fill=BOTH, expand=True)
        
        max_year = "The latest song was recorded in %d" % db_max(DB, 'year')
        self.max_year_label = Label(master, text = max_year)
        self.data.append(max_year)
        self.max_year_label.pack(side=TOP, fill=BOTH, expand = True)
        
        self.save_btn = Button(master, text="Save", command=self.save)
        self.save_btn.pack(side=TOP, fill=BOTH, expand=True)
        
    def save(self):
        filename=hash(str(self.database)) 
        path = "../Data/" + str(filename) + ".txt"
        file = open(path, "w")
        file.writelines(map(lambda x: x + '\n', self.data))
        file.close()