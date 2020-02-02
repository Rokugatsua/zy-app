from Tkinter import *

import UI.enofaref as enofaref, UI.efakturex as efakturex

import scr.dacon as dacon

class UI:
    class menubar:
        def __init__(self, master=None, menubar=Menu):
            self.master = master
            self.menubar = menubar
            self.command = UI.command(self.master)

        def filemenu(self):
            filemenu = Menu(self.menubar, tearoff=0)
            filemenu.add_command(label="", command=None)
            self.menubar.add_cascade(label="File",menu=filemenu)

        def addmenu(self):
            addmenu = Menu(self.menubar, tearoff=0)
            addmenu.add_command(label="Enofa Ref", command = self.command.enofaref)
            addmenu.add_command(label="Efaktur Export", command = self.command.efakturex)
            self.menubar.add_cascade(label="Add", menu=addmenu)

        def helpmenu(self):
            helpmenu = Menu(self.menubar, tearoff=0)
            helpmenu.add_command(label="About", command = None)
            self.menubar.add_cascade(label="Help", menu=helpmenu)



    class command:
        def __init__(self, master=None):
            self.master = master

        def enofaref(self):
            # open UI enofa ref
            enofaref.UI(self.master)

        def efakturex(self):
            # open UI efaktur export
            efakturex.UI(self.master)

class get:
    def __init__(self):
        self.O = dacon.Out()
    def list_csv(self):
        list_csv = self.O.list().csv()
        return list_csv

class save:
    def __init__(self):
        self.I = dacon.In()
    def enofa_number(self, enofa_awal, enofa_akhir):
        pass
        