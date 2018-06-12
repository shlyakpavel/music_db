
from tkinter import Frame, SUNKEN, Label, Entry, Button, TOP
from db import db_get_keys
class InsertionFrame(Frame):
    """
        
    Author:Andrew
    """
    e = {}
    prev_item = None
    def __init__(self, master, app, DB, prev_item = None):
        Frame.__init__(self, master, borderwidth=1, relief=SUNKEN)
        #l = Label(master, text="This is window")
        #l.pack(side=TOP, fill=BOTH, expand=True)
        self.db = DB
        self.prev_item = prev_item
        #self.e = {}
        for i in db_get_keys(self.db):
            l = Label(master, text=i)
            l.pack(side=TOP, fill="none", expand=False)
            self.e[i] = Entry(master)
            self.e[i].pack(side=TOP, fill="none", expand=False)
            if prev_item:
                self.e[i].insert(0,prev_item[i])
        add_button=Button(master, text="Save", command=self.obrabotchik)
        add_button.pack(side=TOP, fill="none", expand=False)
        self.app = app
        
    def obrabotchik(self):
        """This method is called then button is clicked
        Author: Andrew
        Edited by Pavel on 12.07
        """
        item = {}
        for i in db_get_keys(self.db):
            item[i] = self.e[i].get()
            #print(self.e[i].get())
        #mas
        self.app.insert_item(item, self.prev_item)
        
