from tkinter import Frame, SUNKEN, Entry, Button, BOTTOM, OptionMenu, \
    StringVar
from db import db_get_keys, db_list_greater_than, db_create, db_add_entry
class FilterFrame(Frame):
    """
    Author: Pavel
    """
    e = {}
    filter_count = 0
    filters = []
    
    def __init__(self, master, app, DB):
        Frame.__init__(self, master, borderwidth=1, relief=SUNKEN)
        self.database = DB
        self.master = master
        add_button = Button(master, text="+", command=self.draw_filter)
        add_button.pack(side=BOTTOM, fill="none", expand=False)
        apply_button = Button(master, text="apply", command=self.apply)
        apply_button.pack(side=BOTTOM, fill="none", expand=False)
        self.draw_filter()
        self.app = app

    def draw_filter(self):
        field = StringVar(self)
        criteria = StringVar(self)
        #variable.set("one") # default value
        fields = OptionMenu(self, field, *db_get_keys(self.database))
        fields.grid(row=self.filter_count, column=1)
        criteria_box = OptionMenu(self, criteria, *self.citeria_dict.keys())
        criteria_box.grid(row=self.filter_count, column=2)
        data_entry = Entry(self)
        data_entry.grid(row=self.filter_count, column=3)
        self.filters.append({'field':field, 'criteria': criteria, 'data': data_entry})
        self.filter_count += 1
        
    def apply(self):
        new_db = self.database
        for filt in self.filters:
            field = filt['field'].get()
            data = filt['data'].get()
            new_db = self.citeria_dict[filt['criteria'].get()](self, new_db, field, data)
        print(new_db)
        self.app.apply_db(new_db)
            
            
    def gt(self, old_db, field, data):
        new_db = db_create()
        items = db_list_greater_than(self.database, field, int(data))
        for i in items:
            db_add_entry(new_db, i)
        return new_db
    
    def lt(self, old_db, field, data):
        new_db = db_create()
        items = db_list_greater_than(self.database, field, int(data))
        for i in items:
            db_add_entry(new_db, i)
        return new_db
    
    def eq(self, old_db, field, data):
        print("EQ")
        
    def inc(self, old_db, field, data):
        print("INC")
        
    citeria_dict = {"Greater then":gt, "Less then": lt, "Is equal to" : eq, "Includes":inc}
        