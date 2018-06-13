"""This module is responsible for GUI
Everything that is drown by our app should be done here
However, custom widgets can be stored in external modules
"""
import tkinter as tk
from tkinter import END, BOTH, RIGHT, BOTTOM, LEFT, RAISED, Button, Frame, \
    X, YES, TOP
from MultiListbox import MultiListbox
from db import db_get_keys, db_load, db_store, db_find_strict, db_delete_entry, \
    db_create, db_add_entry
from add_dialog import InsertionFrame
from stframe import StatsFrame
from filter import FilterFrame

try:
    DB = db_load("db.pickle")
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
        self.toolbar = Frame(self.master, bd=1, relief=RAISED)
        #A button to add new song
        add_button = Button(self.toolbar, command=self.add_item)
        add_button["text"] = "+"
        add_button.pack(side=LEFT, padx=2, pady=2)
        #A button to remove a song
        remove_button = Button(self.toolbar, command=self.remove_items)
        remove_button["text"] = "-"
        remove_button.pack(side=LEFT, padx=2, pady=2)
        
        edit_button = Button(self.toolbar, command=self.edit_item)
        edit_button["text"] = "Edit"
        edit_button.pack(side=LEFT, padx=2, pady=2)

        search_button = Button(self.toolbar, command=self.create_filters)
        search_button["text"] = "Search"
        search_button.pack(side=LEFT, padx=2, pady=2)

        self.stats_button = Button(self.toolbar, command=self.stats)
        self.stats_button["text"] = "Stats"
        self.stats_button.pack(side=LEFT, padx=2, pady=2)

        #Idk what it is for
        exit_button = Button(self.toolbar, fg="red", command=ROOT.destroy)
        exit_button["text"] = "Quit"
        exit_button.pack(side=RIGHT, padx=2, pady=2)
        self.toolbar.pack(side=BOTTOM, fill=X)

        keys = ((i, 0) for i in db_get_keys(DB))
        self.table = MultiListbox(ROOT, keys)
        del keys
        self.apply_db(DB)
        self.table.pack(expand=YES, fill=BOTH, side=BOTTOM)

    def remove_items(self):
        """A method to delete item then - button is pressed
        Author: Pavel"""
        items = self.table.curselection()
        for index in items:
            item = self.table.get(index)
            items_in_db = db_find_strict(DB, dict(zip(db_get_keys(DB), item)))
            print(items_in_db)
            for item_in_db in items_in_db:
                db_delete_entry(DB, item_in_db)
                print(item_in_db)
            #search and delete in db
            self.table.delete(index)

    def edit_item(self):
        """A method to open "Edit entry" dialog
        Author: Pavel"""
        
        edit_indexes = self.table.curselection()
        if not edit_indexes:
            return
        self.edit_index = edit_indexes [0]
        item = self.table.get(self.edit_index)
        item = list(db_find_strict(DB, dict(zip(db_get_keys(DB), item))).values())[0]
        print(item)
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
        stats_frame = StatsFrame(stats_window, self.FILTERED_DB)
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
        db_add_entry(DB, item)
        self.table.insert(where, tuple(item.values()))
    
    def create_filters(self):
        """Create filter
        Author: Pavel
        """
        filter_window = tk.Toplevel(self)
        filter_window.wm_title("Add filters")
        filter_frame = FilterFrame(filter_window, self,  DB)
        filter_frame.pack(side=TOP, fill=BOTH, expand=True)
        
    
    def apply_db(self, data):
        """Display db
        Author: Pavel"""
        self.FILTERED_DB = data
        self.table.delete(0, END)
        for i in data.values():
            self.table.insert(END, tuple(i.values()))
            
ROOT = tk.Tk()
ROOT.title('MYSQL killer for music')
APP = Application(master=ROOT)
APP.mainloop()
db_store(DB, "db.pickle")
