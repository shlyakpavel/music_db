"""This module is responsible for GUI
Everything that is drown by our app should be done here
However, custom widgets can be stored in external modules
"""
import sys
sys.path.append('../Library')

import tkinter as tk
from tkinter import END, BOTH, RIGHT, BOTTOM, LEFT, RAISED, Button, Frame, \
    X, YES, TOP, DISABLED, NORMAL
from MultiListbox import MultiListbox
from db import db_get_keys, db_load, db_store, db_find_strict, db_delete_entry, \
    db_create, db_add_entry
from add_dialog import InsertionFrame
from stframe import StatsFrame
from filter import FilterFrame
from config import Button_color, Frame_color, Text_color

DB_PATH = "../Data/db.pickle"

try:
    DB = db_load(DB_PATH)
except FileNotFoundError:
    DB = db_create()


class Application(tk.Frame):
    """Main application class.
    Author: Pavel"""

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """A method to draw the interface
        Should be only called in class constructor
        Author: Pavel"""
        self.toolbar = Frame(self.master, bg=Frame_color, bd=1, relief=RAISED)
        #A button to add new song
        add_button = Button(self.toolbar, bg=Button_color, fg=Text_color, command=self.add_item)
        add_button["text"] = "+"
        add_button.pack(side=LEFT, padx=2, pady=2)
        #A button to remove a song
        remove_button = Button(self.toolbar, bg=Button_color, fg=Text_color, command=self.remove_items)
        remove_button["text"] = "-"
        remove_button.pack(side=LEFT, padx=2, pady=2)

        edit_button = Button(self.toolbar, bg=Button_color, fg=Text_color, command=self.edit_item)
        edit_button["text"] = "Edit"
        edit_button.pack(side=LEFT, padx=2, pady=2)

        search_button = Button(self.toolbar, bg=Button_color, fg=Text_color, command=self.create_filters)
        search_button["text"] = "Search"
        search_button.pack(side=LEFT, padx=2, pady=2)

        stats_button = Button(self.toolbar, bg=Button_color, fg=Text_color, command=self.stats)
        stats_button["text"] = "Stats"
        stats_button.pack(side=LEFT, padx=2, pady=2)
        
        self.reset_button = Button(self.toolbar, bg=Button_color, fg=Text_color, command=self.reset_db)
        self.reset_button["text"] = "Reset filters"
        self.reset_button.pack(side=LEFT, padx=2, pady=2)

        #Idk what it is for
        exit_button = Button(self.toolbar, bg=Button_color, fg="red", command=ROOT.destroy)
        exit_button["text"] = "Quit"
        exit_button.pack(side=RIGHT, padx=2, pady=2)
        self.toolbar.pack(side=BOTTOM, fill=X)

        self.keys = db_get_keys()
        keys_tmp = ((i, 0) for i in self.keys)
        self.table = MultiListbox(ROOT, keys_tmp)
        del keys_tmp
        self.apply_db(DB, True)
        self.table.pack(expand=YES, fill=BOTH, side=BOTTOM)

    def remove_items(self):
        """A method to delete item then - button is pressed
        Author: Pavel"""
        items = self.table.curselection()
        for index in items:
            item = self.table.get(index)
            del item[-1]
            items_in_db = db_find_strict(DB, dict(zip(db_get_keys(DB), item)))
            for item_in_db in items_in_db:
                db_delete_entry(DB, item_in_db)
            #search and delete in db
            self.table.delete(index)

    def edit_item(self):
        """A method to open "Edit entry" dialog
        Author: Pavel"""
        edit_indexes = self.table.curselection()
        if not edit_indexes:
            return
        self.edit_index = edit_indexes[0]
        item = self.table.get(self.edit_index)
        time = item[-1]
        del item[-1]    #DURATION
        item = list(db_find_strict(DB, dict(zip(db_get_keys(DB), item))).values())[0]
        item['duration'] = time
        t = tk.Toplevel(self)
        t.wm_title("Add track to DB")
        l = InsertionFrame(t, self, DB, item)
        l.pack(side="top", fill="both", expand=True)

    def add_item(self):
        """A simple method to add entry
        Author: Andrew"""
        t = tk.Toplevel(self)
        t.wm_title("Add track to DB")
        l = InsertionFrame(t, self, DB)
        l.pack(side="top", fill="both", expand=True)

    def stats(self):
        """Statistics
        Author: Pavel"""
        stats_window = tk.Toplevel(self)
        stats_window.wm_title("Stats")
        stats_frame = StatsFrame(stats_window, self.filtered_db)
        stats_frame.pack(side=TOP, fill=BOTH, expand=True)

    def insert_item(self, item, prev_item):
        """A so-called slot to insert item as soon as it is created
        Author: Andrew"""
        where = END
        if prev_item:
            to_delete = list(db_find_strict(DB, prev_item))[0]
            db_delete_entry(DB, to_delete)
            self.table.delete(self.edit_index)
            where = self.edit_index
        res = []
        for key in self.keys:
            res.append(item[key])
        self.table.insert(where, res)
        secs = 0
        for a, b in enumerate(reversed(item['duration'].split(':'))):
            secs += 60**int(a) * int(b)
        item['duration'] = secs
        db_add_entry(DB, item)

    def create_filters(self):
        """Create filter
        Author: Pavel
        """
        filter_window = tk.Toplevel(self)
        filter_window.wm_title("Add filters")
        filter_frame = FilterFrame(filter_window, self, DB)
        filter_frame.pack(side=TOP, fill=BOTH, expand=True)

    def apply_db(self, data, clear = False):
        """Display db
        Author: Pavel"""
        if clear:
            self.reset_button['state'] = DISABLED
        else:
            self.reset_button['state'] = NORMAL
        self.filtered_db = data
        self.table.delete(0, END)
        for i in data.values():
            try:
                j = i.copy()
                m, s = divmod(int(i['duration']), 60)
                h, m = divmod(m, 60)
                j['duration'] = "%d:%02d:%02d" % (h, m, s)
            except ValueError:
                i['duration'] = 0
                j['duration'] = 0
            res = []
            for key in self.keys:
                res.append(j[key])
            self.table.insert(END, res)
    def reset_db(self):
        self.filtered_db = DB
        self.apply_db(self.filtered_db, True)
        
        

ROOT = tk.Tk()
ROOT.title('MYSQL killer for music')
APP = Application(master=ROOT)
APP.mainloop()
db_store(DB, DB_PATH)
