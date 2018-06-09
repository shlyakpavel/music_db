"""This module is responsible for GUI
Everything that is drown by our app should be done here
However, custom widgets can be stored in external modules
"""
import tkinter as tk
from tkinter import END, BOTH, TOP, YES
from MultiListbox import MultiListbox
from db import db_get_keys, db_load

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
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side=TOP)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=ROOT.destroy)
        self.quit.pack(side="bottom")
        keys = zip(db_get_keys(DB),[40,20,20,20]) #TODO: automatic sizes
        self.table = MultiListbox(self, list(keys))
        for i in DB.values():
            self.table.insert(END, tuple(i.values()))
        self.table.pack(expand=YES, fill=BOTH, side=TOP)
        #self.box = tk.Listbox(self);
        #self.box.pack(side="bottom")
        #for i in db_to_str_list(db):
        #    print(i)
        #    self.box.insert(1,i)
    def say_hi(self):
        """A simple method to show that button is pressed
        Author: unknown hacker"""
        print("hi there, everyone!")

ROOT = tk.Tk()
APP = Application(master=ROOT)
APP.mainloop()
