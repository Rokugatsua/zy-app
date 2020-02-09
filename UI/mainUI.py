from Tkinter import *

from UI import cfgUI

TITLE = 'Zy Project' #default title information if something Error
WINRES = "600x500"

def run(app_info = None):
    global TITLE
    if app_info is not None :
        TITLE = app_info
    print(TITLE)

    #run UI with Tkinter module
    root = Tk()
    app = Application(root)
    app.mainloop()

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.pack()
        self.initUI()
        self.mainbar()
        self.wraper()

    def initUI(self):
        self.master.title(TITLE)
        self.master.geometry(WINRES)

    def mainbar(self):
        menubar = Menu(self)
        # making menuUI with their self class, for easy improvement in future
        menuUI = cfgUI.UI.menubar(self,menubar) #initialize
        menuUI.filemenu()
        menuUI.addmenu()
        self.master.config(menu=menubar)

    def wraper(self):
        # like ass Wraper in web, this a main frame of the application
        headframe = Frame(self)
        headframe.pack()
        get = cfgUI.get()
        self.enofaref = get.list_enofa_ref()
        self.option = [str(lb[5]) for lb in self.enofaref]
        self.tname = [str(lb[1]) for lb in self.enofaref]

        self.va = StringVar()
        self.va.set(self.option[0])
        head_om = apply(OptionMenu, (headframe, self.va) + tuple(self.option))
        head_om.pack()

        head_btn = Button(headframe, text = "refresh",command=self.refresh)
        head_btn.pack()
        self.listing_data()

    def listing_data(self):
        listframe = Frame(self)
        listframe.pack()
        
        lb = self.va.get()
        ix = self.option.index(lb)

        tname = self.tname[ix]
        get = cfgUI.get()
        data = get.list_enofa_list(tname)
        datali = [str(li[0]) for li in data if li[1] == 0]
        self.libox = Listbox(listframe)

        for li in datali:
            self.libox.insert(END,li)

        self.libox.pack()

    def refresh(self):
        lb = self.va.get()
        ix = self.option.index(lb)

        tname = self.tname[ix]
        get = cfgUI.get()
        data = get.list_enofa_list(tname)
        datali = [str(li[0]) for li in data if li[1] == 0]
        self.libox.delete(0,END)

        for li in datali:
            self.libox.insert(END,li)





if __name__ == "__main__":
    run()


