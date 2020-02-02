from Tkinter import *

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
        pass