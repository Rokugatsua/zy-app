from Tkinter import *

try:
    import UI.cfgUI as cfgUI
except:
    import cfgUI

TITLE = 'Add Efaktur Export'
WINRES = '600x400'

class UI:
    def __init__(self, parent=None):
        self.win = Toplevel(parent)
        self.initUI()
        self.form()

    def initUI(self):
        self.win.title(TITLE)
        self.win.geometry(WINRES)

    def form(self):
        formframe = Frame(self.win)
        formframe.pack(side=TOP)
        bottomframe = Frame(self.win)
        bottomframe.pack(side=BOTTOM)

        scroller = Scrollbar(formframe)
        scroller.pack(side=RIGHT, fill=Y)

        self.libox = Listbox(formframe, yscrollcommand = scroller.set)
        self.show_list()

        self.libox.pack(side=LEFT, fill=BOTH)
        scroller.config(command=self.libox.yview)

        btn_add = Button(bottomframe, text="Add", command = None)
        btn_add.pack()

    def show_list(self):
        li_data = ["",""]
        get = cfgUI.get()
        li_data = get.list_csv()
        for li in li_data:
            self.libox.insert(END,li)

    def refresh(self):
        self.libox.delete(0,END)
        self.show_list()