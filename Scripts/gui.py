"""This module is responsible for GUI
Everything that is drown by our app should be done here
However, custom widgets can be stored in external modules
"""
import tkinter as tk
from tkinter import END, BOTH, RIGHT, BOTTOM, LEFT, RAISED, Button, Frame, \
    X, FLAT, YES
from MultiListbox import MultiListbox
from db import db_get_keys, db_load, db_store, db_find_strict, db_delete_entry

DB = db_load("db.pickle")

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
        self.add_button = Button(self.toolbar, relief=FLAT, command=ROOT.destroy)
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
            items_in_db = db_find_strict(DB, dict(zip(list(db_get_keys(DB)),list(item))))
            print(items_in_db)
            for item_in_db in items_in_db:
                db_delete_entry(DB, item_in_db)
                print(item_in_db)
            #search and delete in db
            self.table.delete(index)
        
    def say_hi(self):
        """A simple method to show that button is pressed
        Author: unknown hacker"""
        print("hi there, everyone!")

ROOT = tk.Tk()
ROOT.title('MYSQL killer for music')
APP = Application(master=ROOT)
APP.mainloop()
db_store(DB, "db.pickle")
