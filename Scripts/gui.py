"""This module is responsible for GUI
Everything that is drown by our app should be done here
However, custom widgets can be stored in external modules
"""
import tkinter as tk
from tkinter import END, BOTH, RIGHT, BOTTOM, LEFT, RAISED, Button, Frame, \
    X, FLAT, YES
from MultiListbox import MultiListbox
from db import db_get_keys, db_load, db_store, db_find_strict, db_delete_entry, \
    db_create
from add_dialog import InsertionFrame
from stframe import InsertionFrame

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

        self.search_button = Button(self.toolbar, relief=FLAT, command=ROOT.destroy)
        self.search_button["text"] = "Search" #TODO: icon
        self.search_button.pack(side=LEFT, padx=2, pady=2)

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
        
    def add_item(self):
        """A simple method to add entry
        Author: Pavel"""
        t = tk.Toplevel(self)
        t.wm_title("Window")
        l = InsertionFrame(t)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        
    def stats(self):
        """Statistics
        Author: Pavel"""
        t = tk.Toplevel(self)
        t.wm_title("Window")
        l = StatsFrame(t)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        
ROOT = tk.Tk()
ROOT.title('MYSQL killer for music')
APP = Application(master=ROOT)
APP.mainloop()
db_store(DB, "db.pickle")
