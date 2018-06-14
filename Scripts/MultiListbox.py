from tkinter import PanedWindow, Frame, Tk, Label, TOP, SUNKEN, LEFT,\
    YES, BOTH, GROOVE, X, Listbox, FLAT, FALSE, MULTIPLE, Scrollbar, VERTICAL,\
    Y, RIGHT, NO, END, SCROLL, PAGES
    
from config import ListBox_color

#def cmp(a, b):
#    """python 3 replacement for python 2 cmp function"""
#    return (a > b) - (a < b)

class MultiListbox(PanedWindow):
    """This class is supposed to display a table
    Author: Pavel Shlyak"""
    direction = True
    def __init__(self, master, lists):
        """MultiListbox class constructor
        Args:
            master - parent view
            lists - columns
        Author: Pavel"""
        PanedWindow.__init__(self, master, borderwidth=1, showhandle=False, 
                             sashwidth=2, sashpad=0, relief=SUNKEN)
        self.lists = []
        self.columns = []
        for l, w in lists:
            self.columns.append(l)
            frame = Frame(self)
            frame.pack(side=LEFT, expand=YES, fill=BOTH)
            tl = Label(frame, text=l, borderwidth=2, relief=GROOVE)
            tl.pack(fill=X)
            tl.bind('<Button-1>', self.clickon)
            lb = Listbox(frame, bg = ListBox_color, width=w, borderwidth=0, 
                         selectborderwidth=0, relief=FLAT, exportselection=FALSE, 
                         selectmode=MULTIPLE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind('<B1-Motion>', lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>', lambda e, s=self: s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self: s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self: s._button2(e.x, e.y))
            lb.bind('<Button-4>', lambda e, s=self: s._scroll(SCROLL, 1, PAGES))
            lb.bind('<Button-5>', lambda e, s=self: s._scroll(SCROLL, -1, PAGES))
            self.add(frame)
        Label(master, borderwidth=1, relief=FLAT).pack(fill=X)
        sb = Scrollbar(master, orient=VERTICAL, command=self._scroll, borderwidth=1)
        sb.pack(fill=Y, side=RIGHT, expand=NO)
        for l in self.lists:
            l['yscrollcommand'] = sb.set
        #self.add(frame)
        self.pack(expand=YES, fill=BOTH)
        self.sorted_by = -1
        self.previousWheel = 0


    def _select(self, y, state=16):
        row = self.lists[0].nearest(y)
        if state == 16:
            self.selection_clear(0, END)
        self.selection_set(row)
##        print(self.curselection())
        return 'break'


    def _button2(self, x, y):
        for l in self.lists:
            l.scan_mark(x, y)
        return 'break'


    def _b2motion(self, x, y):
        for current_list in self.lists:
            current_list.scan_dragto(x, y)
        return 'break'


    def _scroll(self, *args):
        """Private scroll method to scroll all lists at once
        Author: Pavel"""
        for current_list in self.lists:
            current_list.yview(*args)
        return 'break'


    def clickon(self, event):
        """A sort button handler"""
        self._sort_by(self.columns.index(event.widget['text']))


    def _sort_by(self, column):
        """ Sort by a given column. """
        if column == self.sorted_by:
            direction = not self.direction
        else:
            direction = False

        elements = self.get(0, END)
        self.delete(0, END)
        #elements = list(elements)
        #elements.sort(lambda x, y: self._sortAssist(column, direction, x, y))
        elements.sort(reverse=direction, key=lambda elements: elements[column])
        self.insert(END, *elements)

        self.sorted_by = column
        self.direction = direction


#    def _sortAssist(self, column, direction, x, y):
#        c = cmp(x[column], y[column])
#        if c:
#            return direction * c
#        else:
#            return direction * cmp(x, y)

    def curselection(self):
        return self.lists[0].curselection()


    def delete(self, first, last=None):
        """Delete a line or a line sequence
        Author: Pavel Shlyak"""
        for current_list in self.lists:
            current_list.delete(first, last)


    def get(self, first, last=None):
        result = []
        for current_list in self.lists:
            result.append(current_list.get(first, last))
        if last:
            return list(zip(*result))
        return result


    def index(self, index):
        self.lists[0].index(index)


    def insert(self, index, *elements):
        """Insert an element
        Args:
            index - index where to insert it
            elements - tuple like
                (('Twenty one pilots', 'Heathens', 'Suicide Squad'),)
        Author: Pavel
        """
        for element in elements:
            for current_column, current_list in enumerate(self.lists):
                current_list.insert(index, element[current_column])


    def size(self):
        return self.lists[0].size()


    def see(self, index):
        for current_list in self.lists:
            current_list.see(index)

    def selection_anchor(self, index):
        for current_list in self.lists:
            current_list.selection_anchor(index)


    def selection_clear(self, first, last=None):
        for current_list in self.lists:
            current_list.selection_clear(first, last)


    def selection_includes(self, index):
        return self.lists[0].selection_includes(index)


    def selection_set(self, first, last=None):
        """Set selection on a line or a line sequence
        Args:
            first - the first line of the selection area
            last - the last line of the selection area (optional)
        Author: Pavel
        """
        for current_list in self.lists:
            current_list.selection_set(first, last)
        print(self.curselection())


if __name__ == '__main__':
    ROOT = Tk()
    Label(ROOT, text='MultiListbox').pack(side=TOP)
    MLB = MultiListbox(ROOT, (('Subject', 40), ('Sender', 20), ('Date', 10)))
    for i in range(5000):
        MLB.insert(END,
                   ('Important Message: %d' % i, 'John Doe %d' % (10000 - i),
                    '10/10/%04d' % (1900+i)))
        MLB.pack(expand=YES, fill=BOTH, side=TOP)
    ROOT.mainloop()
