from tkinter import Frame, SUNKEN, Label, Button, TOP, BOTH
from db import db_mean, db_max, db_min, db_keys_to_list
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
        
        min_year = "The eldest song was recorded in %d" % db_min(DB, 'year')
        self.min_year_label = Label(master, text = min_year)
        self.data.append(min_year)
        self.min_year_label.pack(side=TOP, fill=BOTH, expand = True)

        ms_year = "Most songs were recorded in %d" % db_min(DB, 'year') #TODO
        self.ms_year_label = Label(master, text = ms_year)
        self.data.append(ms_year)
        self.ms_year_label.pack(side=TOP, fill=BOTH, expand = True)
        
        unique_artists = "Artists: %d" % self.art_count()
        self.unique_artists_label = Label(master, text = unique_artists)
        self.data.append(unique_artists)
        self.unique_artists_label.pack(side=TOP, fill=BOTH, expand = True)
        
        self.save_btn = Button(master, text="Save", command=self.save)
        self.save_btn.pack(side=TOP, fill=BOTH, expand=True)
        
    def art_count(self):
        lst = db_keys_to_list(self.database,'interpreter')
        lst = set(lst)
        return len(lst)
        
    def save(self):
        filename=hash(str(self.database)) 
        path = "../Data/" + str(filename) + ".txt"
        file = open(path, "w")
        file.writelines(map(lambda x: x + '\n', self.data))
        file.close()