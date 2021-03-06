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
        Frame.__init__(self, master, borderwidth=1, relief=SUNKEN, bg=Frame_color)

        entries_amount = "Songs: %d" % len(DB.items())
        amount_label = Label(self, text=entries_amount)
        self.data.append(entries_amount)
        amount_label.pack(side=TOP, fill=BOTH, expand=True)

        mean_year = "Mean year: %d" % db_mean(DB, 'year')
        mean_year_label = Label(self, text=mean_year)
        self.data.append(mean_year)
        mean_year_label.pack(side=TOP, fill=BOTH, expand=True)

        max_year = "The latest song was recorded in %d" % db_max(DB, 'year')
        max_year_label = Label(self, text=max_year)
        self.data.append(max_year)
        max_year_label.pack(side=TOP, fill=BOTH, expand=True)

        min_year = "The eldest song was recorded in %d" % db_min(DB, 'year')
        min_year_label = Label(self, text=min_year)
        self.data.append(min_year)
        min_year_label.pack(side=TOP, fill=BOTH, expand=True)

        ms_year = "Most songs were recorded in " + db_most(DB, 'year')
        ms_year_label = Label(self, text=ms_year)
        self.data.append(ms_year)
        ms_year_label.pack(side=TOP, fill=BOTH, expand=True)

        unique_artists = "Artists: %d" % self.art_count()
        unique_artists_label = Label(self, text=unique_artists)
        self.data.append(unique_artists)
        unique_artists_label.pack(side=TOP, fill=BOTH, expand=True)

        mean_dur = "Mean duration (sec): %d" % db_mean(DB, 'duration')
        mean_dur_label = Label(self, text=mean_dur)
        self.data.append(mean_dur)
        mean_dur_label.pack(side=TOP, fill=BOTH, expand=True)

        #Dispersion db_dispersion
        dur_disp = "Duration dispersion: %d" % db_dispersion(DB, 'duration')
        dur_disp_label = Label(self, text=dur_disp)
        self.data.append(dur_disp)
        dur_disp_label.pack(side=TOP, fill=BOTH, expand=True)

        save_btn = Button(self, text="Save", command=self.save, \
                               bg=Button_color, fg=Text_color)
        save_btn.pack(side=TOP, fill=BOTH, expand=True)

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
