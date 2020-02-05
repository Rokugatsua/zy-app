from Tkinter import *
import cfgUI

TITLE = 'Create New DB'
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

        self.var_namedb = StringVar()
        self.var_namedb.set("")

        notice = Label(formframe, text="input your name database")
        notice.pack()
        fl = LabelFrame(formframe, text="Create New Database")
        fl.pack()
        e_db = Entry(fl, textvariable=self.var_namedb)
        e_db.pack()
        self.var_namedb.trace("w",self.tracing_value)

        self.var_rb_set = BooleanVar()
        self.var_rb_set.set(False)
        self.rb_set = Checkbutton(formframe, text=" Keep this database to default", onvalue = True,offvalue=False,variable=self.var_rb_set)
        self.rb_set.pack()

        btn_save = Button(bottomframe, text="Save", command=self.save_db)
        btn_save.pack()

    def save_db(self):
        varname = self.var_namedb.get()
        ondefault = self.var_rb_set.get()
        save = cfgUI.save()
        save.createdb(varname,ondefault)
        # function under development for send variable enofa awal and akhir for save in db

    def tracing_value(self, *args):
        var_a = self.var_namedb.get()
        if var_a.endswith('.db'):
            var_a = var_a
            self.var_namedb.set(var_a)
        else:
            var_a = var_a + ".db"
            self.var_namedb.set(var_a)




