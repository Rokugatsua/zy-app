import config
from UI import mainUI
from scr import dacon

class RunApplication(): # Main class for run this application.
    def __init__(self):
        self.check_initialize()
        self.run(self.get_info())

    def check_initialize(self):
        onReady =  dacon.OnReady()
        check_init = onReady.check_init()
        print(check_init)


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
