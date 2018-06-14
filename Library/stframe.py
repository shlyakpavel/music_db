"""
This module provides a class for gathering and displaying statistics
Author: Pavel
Maintainer: Pavel
"""
from tkinter import Frame, SUNKEN, Label, Button, TOP, BOTH
from db import db_mean, db_max, db_min, db_most, db_keys_to_list, \
    db_dispersion
from config import Button_color, Frame_color, Text_color
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
        Frame.__init__(self, master, borderwidth=1, relief=SUNKEN, bg = Frame_color)

        entries_amount = "Songs: %d" % len(DB.items())
        self.amount_label = Label(master, text=entries_amount)
        self.data.append(entries_amount)
        self.amount_label.pack(side=TOP, fill=BOTH, expand=True)

        mean_year = "Mean year: %d" % db_mean(DB, 'year')
        self.mean_year_label = Label(master, text=mean_year)
        self.data.append(mean_year)
        self.mean_year_label.pack(side=TOP, fill=BOTH, expand=True)

        max_year = "The latest song was recorded in %d" % db_max(DB, 'year')
        self.max_year_label = Label(master, text=max_year)
        self.data.append(max_year)
        self.max_year_label.pack(side=TOP, fill=BOTH, expand=True)

        min_year = "The eldest song was recorded in %d" % db_min(DB, 'year')
        self.min_year_label = Label(master, text=min_year)
        self.data.append(min_year)
        self.min_year_label.pack(side=TOP, fill=BOTH, expand=True)

        ms_year = "Most songs were recorded in " + db_most(DB, 'year')
        self.ms_year_label = Label(master, text=ms_year)
        self.data.append(ms_year)
        self.ms_year_label.pack(side=TOP, fill=BOTH, expand=True)

        unique_artists = "Artists: %d" % self.art_count()
        self.unique_artists_label = Label(master, text=unique_artists)
        self.data.append(unique_artists)
        self.unique_artists_label.pack(side=TOP, fill=BOTH, expand=True)
        
        mean_dur = "Mean duration (sec): %d" % db_mean(DB, 'duration')
        self.mean_dur_label = Label(master, text=mean_dur)
        self.data.append(mean_dur)
        self.mean_dur_label.pack(side=TOP, fill=BOTH, expand=True)
        
        #Dispersion db_dispersion
        dur_disp = "Duration dispersion: %d" % db_dispersion(DB, 'duration')
        self.dur_disp_label = Label(master, text=dur_disp)
        self.data.append(dur_disp)
        self.dur_disp_label.pack(side=TOP, fill=BOTH, expand=True)

        self.save_btn = Button(master, text="Save", command=self.save, bg = Button_color, fg = Text_color)
        self.save_btn.pack(side=TOP, fill=BOTH, expand=True)

    def art_count(self):
        """Counts amount of artists in DB
        Returns amount(int)
        Author: Pavel"""
        lst = db_keys_to_list(self.database, 'artist')
        #Sets cannot have duplicate entries. Thus, we convert list to a set
        lst = set(lst)
        return len(lst)

    def save(self):
        """This method is used to save analysis result
        Author: Pavel"""
        filename = hash(str(self.database))
        path = "../Output/" + str(filename) + ".txt"
        file = open(path, "w")
        file.writelines(map(lambda x: x + '\n', self.data))
        file.close()
