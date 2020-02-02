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
        pass



if __name__ == "__main__":
    run()


