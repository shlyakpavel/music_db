import tkinter as tk
import pickle


db = pickle.load(open("db.pickle","rb"))

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")
        self.box = tk.Listbox(self);
        self.box.pack(side="bottom")
        #for i in db:
        #    tmp = db[i]
        #    print(tmp)
        #    if 'interpreter' in tmp: self.box.insert(1,tmp['interpreter'])
        for i in db_to_str_list(db):
            print(i)
            self.box.insert(1,i)
    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
