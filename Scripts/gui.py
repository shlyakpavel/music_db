import tkinter as tk
from tkinter import END, BOTH, TOP, YES
import pickle
from MultiListbox import MultiListbox

db = pickle.load(open("db.pickle", "rb"))

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side=TOP)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=ROOT.destroy)
        self.quit.pack(side="bottom")
        self.table = MultiListbox(self, (('Interpreter', 40), ('Song', 20), ('Album', 10)))
        for i in db.values():
            self.table.insert(END,
                              (i['interpreter'], i['song'], i['album']))
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
