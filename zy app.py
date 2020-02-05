import config
from UI import mainUI
from scr import dacon

class RunApplication(): # Main class for run this application.
    def __init__(self):
        self.onready =  dacon.OnReady()
        if self.check_initialize():
            print("ready")
            self.run(self.get_info())
        else:
            print("need initialize")
            self.onready
            ReRun()
        

    def check_initialize(self):
        check_init = self.onready.check_init()
        return check_init


    def get_info(self):
        app_name =  config.cfgInfo.AppName
        app_version = config.cfgInfo.AppVersion + config.cfgInfo.AppStatus
        return app_name, app_version

    def run(self, info):
        self.info = ' - '.join(info)
        mainUI.run(self.info)


def ReRun():
    RunApplication()


if __name__ == "__main__":
    RunApplication()
