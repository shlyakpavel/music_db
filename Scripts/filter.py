from tkinter import Frame, SUNKEN, Entry, Button, TOP, BOTTOM, OptionMenu, \
    StringVar, LEFT
from db import db_get_keys
class FilterFrame(Frame):
    """
        
    Author: Pavel
    """
    e = {}
    citeria_dict = {"Greater then":"gt", "Less then": "lt", "Is equal to" : "eq", "Includes":"inc"}
    filter_count = 0
    def __init__(self, master, app, DB):
        Frame.__init__(self, master, borderwidth=1, relief=SUNKEN)
        self.db = DB
        self.master = master
        add_button=Button(master, text="+", command=self.drawFileter)
        add_button.pack(side=BOTTOM, fill="none", expand=False)
        self.drawFileter()
        self.app = app
        
    def drawFileter(self):
        field = StringVar(self)
        criteria = StringVar(self)
        #variable.set("one") # default value
        fields = OptionMenu(self, field, *db_get_keys(self.db))
        fields.grid(row=self.filter_count, column=1)
        criteria_box = OptionMenu(self, criteria, *self.citeria_dict.keys())
        criteria_box.grid(row=self.filter_count, column=2)
        data_entry = Entry(self)
        data_entry.grid(row=self.filter_count, column=3)
        self.filter_count += 1