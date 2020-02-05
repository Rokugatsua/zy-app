import config
from UI import mainUI
from scr import dacon

class RunApplication(): # Main class for run this application.
    def __init__(self, rerun = True):
        if rerun:
            self.onready =  dacon.OnReady()
            if self.check_initialize():
                cfg_init = config.initialize()
                cfg_init.implemented_setting()
                self.run(self.get_info())
            else:
                print("need initialize")
                self.onready.initialize_app()
                ReRun()
        else:
            print("We Reopen application but have some trouble")
            

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
    RunApplication(rerun=True)


if __name__ == "__main__":
    RunApplication()
