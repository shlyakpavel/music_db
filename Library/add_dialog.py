from tkinter import Frame, SUNKEN, Label, Entry, Button, TOP
from db import db_get_keys
from config import Button_color, Frame_color, Text_color
class InsertionFrame(Frame):

    """

    Author:Andrew
    """
    e = {}
    prev_item = None
    def __init__(self, master, app, DB, prev_item = None):
        Frame.__init__(self, master, borderwidth=1, relief=SUNKEN, bg = Frame_color)
        self.db = DB
        self.prev_item = prev_item
        for i in db_get_keys(self.db):
            l = Label(master, text=i, fg = Text_color)
            l.pack(side=TOP, fill="none", expand=False)
            self.e[i] = Entry(master)
            self.e[i].pack(side=TOP, fill="none", expand=False)
            if prev_item:
                self.e[i].insert(0,prev_item[i])
        add_button=Button(master, text="Save", command=self.obrabotchik, bg = Button_color, fg = Text_color)
        add_button.pack(side=TOP, fill="none", expand=False)
        self.app = app
        self.master = master

    def obrabotchik(self):
        """This method is called then button is clicked
        Author: Andrew
        Edited by Pavel
        """
        item = {}
        for i in db_get_keys(self.db):
            item[i] = self.e[i].get()
        if (item['year'].isdecimal()) and item['duration']:
            self.app.insert_item(item, self.prev_item)
            self.master.destroy()

