from Tkinter import *

import enofaref
import efakturex
import createdb
import selectdb

import scr.dacon as dacon

class UI:
    class menubar:
        def __init__(self, master=None, menubar=Menu):
            self.master = master
            self.menubar = menubar
            self.command = UI.command(self.master)

        def filemenu(self):
            filemenu = Menu(self.menubar, tearoff=0)
            filemenu.add_command(label="New Database", command=self.command.createdb)
            #filemenu.add_command(label="Open Database", command=self.command.selectdb)
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

        def createdb(self):
            createdb.UI(self.master)
        
        def selectdb(self):
            selectdb.UI(self.master)

class get:
    def __init__(self):
        self.O = dacon.Out()
    def list_csv(self):
        list_csv = self.O.list().csv()
        return list_csv

    def list_enofa_ref(self):
        O = dacon.Out.to_db()
        data = O.get_enofa_ref()
        return data
        
    def list_enofa_list(self,tname):
        O = dacon.Out.to_db()
        data = O.get_enofa_list(tname)
        return data

class save:
    def __init__(self):
        self.I = dacon.In()
    def enofa_number(self, enofa_awal, enofa_akhir):
        to_db = self.I.to_db()
        to_db.save_enofa_ref(enofa_awal, enofa_akhir)
    def createdb(self, name, ondefault):
        I = dacon.In.setting()
        I.new_db(name,ondefault)

    def add_enfaktur_export(self, csv_name):
        I = dacon.In()
        I_todb = I.to_db()
        I_todb.save_enofa_list(csv_name)
        