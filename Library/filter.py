"""Filter widget
Provides FilterFrame class
Author: Pavel"""
from tkinter import Frame, SUNKEN, Entry, Button, BOTTOM, OptionMenu, \
    StringVar
from db import db_get_keys, gt, lt, eq, inc
from config import Button_color, Frame_color, Text_color
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
        add_button = Button(master, text="+", command=self.draw_filter, bg = Button_color, fg = Text_color)
        add_button.pack(side=BOTTOM, fill="none", expand=False)
        apply_button = Button(master, text="apply", command=self.apply, bg = Button_color, fg = Text_color)
        apply_button.pack(side=BOTTOM, fill="none", expand=False)
        self.draw_filter()
        self.app = app

    def draw_filter(self):
        """Draw a filter in gui
        It is called once in the beggining
        It is also called then "+" button is pressed
        It doesn't set masks or ranges yet #TODO: fix
        Author: Pavel
        """
        #Add only if previous item is done correctly
        if self.filter_count:
            if (not self.filters[-1]['criteria'].get()) or (not self.filters[-1]['field'].get()):
                return
        field = StringVar(self)
        criteria = StringVar(self)
        #variable.set("one") # default value
        fields = OptionMenu(self, field, '', *db_get_keys(self.database))
        fields.grid(row=self.filter_count, column=1)
        criteria_box = OptionMenu(self, criteria, *self.citeria_dict.keys())
        criteria_box.grid(row=self.filter_count, column=2)
        data_entry = Entry(self)
        data_entry.grid(row=self.filter_count, column=3)
        self.filters.append({'field':field, 'criteria': criteria, 'data': data_entry})
        self.filter_count += 1

    def apply(self):
        """This method is called then "apply" button is pressed
        It is used to process all filters and call their appropriate methods
        Calls parent window to update data
        Author: Pavel"""
        new_db = self.database
        for filt in self.filters:
            criteria = filt['criteria'].get()
            #If criteria is not empty. Otherwise there is no need to apply it
            if criteria:
                field = filt['field'].get()
                if field == 'duration':
                    secs = 0
                    for a, b in enumerate(reversed(filt['data'].get().split(':'))):
                        secs += 60**int(a) * int(b)
                    data = secs
                else:
                    data = filt['data'].get()
                new_db = self.citeria_dict[criteria](new_db, field, data)
        self.app.apply_db(new_db)

    citeria_dict = {">":gt, "<": lt, "=" : eq, "Includes":inc}
