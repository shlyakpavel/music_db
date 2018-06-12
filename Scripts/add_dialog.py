
from tkinter import Frame, SUNKEN, Label, Entry, Button, TOP
from db import db_get_keys
class InsertionFrame(Frame):
    """
        
    Author:Andrew
    """
    e = {}
    def __init__(self, master, app, DB):
        Frame.__init__(self, master, borderwidth=1, relief=SUNKEN)
        #l = Label(master, text="This is window")
        #l.pack(side=TOP, fill=BOTH, expand=True)
        self.db = DB
        #self.e = {}
        for i in db_get_keys(self.db):
            l = Label(master, text=i)
            l.pack(side=TOP, fill="none", expand=False)
            self.e[i] = Entry(master)
            self.e[i].pack(side=TOP, fill="none", expand=False)
            #self.e[i].insert(0,"")
        add_button=Button(master, text="ЖОПА!!!", command=self.obrabotchik)
        add_button.pack(side=TOP, fill="none", expand=False)
        self.app = app
        
    def obrabotchik(self):
        print("BAD ASS")
        item = {}
        for i in db_get_keys(self.db):
            item[i] = self.e[i].get()
            #print(self.e[i].get())
        #mas
        self.app.insert_item(item)
        