"""This module is responsible for GUI
Everything that is drown by our app should be done here
However, custom widgets can be stored in external modules
"""
import tkinter as tk
from tkinter import END, BOTH, RIGHT, BOTTOM, LEFT, RAISED, Button, Frame, \
    X, FLAT, YES, TOP
from MultiListbox import MultiListbox
from db import db_get_keys, db_load, db_store, db_find_strict, db_delete_entry, \
    db_create, db_add_entry
from add_dialog import InsertionFrame
from stframe import StatsFrame

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
        self.add_button = Button(self.toolbar, relief=FLAT, command=self.add_item)
        self.add_button["text"] = "+"
        self.add_button.pack(side=LEFT, padx=2, pady=2)
        #A button to remove a song
        self.remove_button = Button(self.toolbar, relief=FLAT, command=self.remove_items)
        self.remove_button["text"] = "-"
        self.remove_button.pack(side=LEFT, padx=2, pady=2)
        
        self.edit_button = Button(self.toolbar, relief=FLAT, command=self.edit_item)
        self.edit_button["text"] = "Edit"
        self.edit_button.pack(side=LEFT, padx=2, pady=2)

        self.search_button = Button(self.toolbar, relief=FLAT, command=ROOT.destroy) #TODO
        self.search_button["text"] = "Search" #TODO: icon
        self.search_button.pack(side=LEFT, padx=2, pady=2)

        self.stats_button = Button(self.toolbar, relief=FLAT, command=self.stats)
        self.stats_button["text"] = "Stats" #TODO: icon
        self.stats_button.pack(side=LEFT, padx=2, pady=2)

        #Idk what it is for
        exit_button = Button(self.toolbar, fg="red", relief=FLAT, command=ROOT.destroy)
        exit_button["text"] = "Quit"
        exit_button.pack(side=RIGHT, padx=2, pady=2)
        self.toolbar.pack(side=BOTTOM, fill=X)

        keys = ((i, 0) for i in db_get_keys(DB))
        self.table = MultiListbox(ROOT, keys)
        del keys
        for i in DB.values():
            self.table.insert(END, tuple(i.values()))
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
        stats_frame = StatsFrame(stats_window, DB)
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

ROOT = tk.Tk()
ROOT.title('MYSQL killer for music')
APP = Application(master=ROOT)
APP.mainloop()
db_store(DB, "db.pickle")
