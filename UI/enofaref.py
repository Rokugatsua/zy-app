from Tkinter import *
import cfgUI

TITLE = 'Add Enofa Refrence'
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

        self.var_enofas = StringVar()
        self.var_enofas.set("")
        self.var_enofae = StringVar()
        self.var_enofae.set("")

        notice = Label(formframe, text=" input without '.' '-' example : 0022012345678")
        notice.pack()
        flenofas = LabelFrame(formframe, text="Enofa Awal")
        flenofas.pack()
        e_enofas = Entry(flenofas, textvariable=self.var_enofas)
        e_enofas.pack()
        self.var_enofas.trace("w",self.tracing_value)

        flenofae = LabelFrame(formframe, text="Enofa Akhir")
        flenofae.pack()
        e_enofae = Entry(flenofae, textvariable=self.var_enofae)
        e_enofae.pack()
        self.var_enofae.trace("w",self.tracing_value)

        btn_save = Button(bottomframe, text="Save", command=self.save_enofa_ref)
        btn_save.pack()

    def save_enofa_ref(self):
        varenofas = self.var_enofas.get()
        varenofae = self.var_enofae.get()

        cfg_save = cfgUI.save()
        cfg_save.enofa_number(varenofas,varenofae)

        # function under development for send variable enofa awal and akhir for save in db

    def tracing_value(self, *args):
        var_a = self.var_enofas.get()
        var_b = self.var_enofae.get()
        if len(var_a) or len(var_b) >= 13:
            self.var_enofas.set(var_a[:13])
            self.var_enofae.set(var_b[:13])




