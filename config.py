import os, json

setting_file = 'setting.json'


# This config the application
class cfgDir:
    BaseDir = os.getcwd()
    UIDir =  os.path.join(BaseDir, "UI")
    ScrDir = os.path.join(BaseDir, "scr")
    DbDir = os.path.join(BaseDir, "db")
    FileDir = os.path.join(BaseDir, "_file")

class cfgInfo:
    # this default info for the app
    AppName = "Zy App"
    AppVersion = "Version 00.0001"
    sts = {"Under Development":"ud","Big Bug":"bb","Stable":"s"}
    AppStatus = sts["Under Development"]
    DATABASE = 'default database.db'
    
class initialize:
    """ initialize the configuratin or setting the application"""
    def __init__(self):
        self.setting_file = setting_file
        self.open_json() #configuratin file used JSON file.
        # Next upgrade will be implemented another file configuration.
        # for best everoiment

    def open_json(self):
        self.setting = {}
        try:
            with open(self.setting_file,'r') as cfgfile:
                cfg_data = json.load(cfgfile)
                self.setting = cfg_data
        except IOError as ie:
            print(ie)
    def get_setting(self):
        return self.setting

    def implemented_setting(self):
        # implemtation the configuration from seting file to this config variable app
        cfgInfo.AppName = self.setting["name"]
        cfgInfo.sts = self.setting["status"]
        cfgInfo.AppVersion = self.setting["version"]
        cfgInfo.DATABASE = self.setting["database"]

    def change_setting(self, name = str, value = str):
        """ Change the setting file with name and the value"""
        self.setting[name] = value
    
    def save_setting(self):
        """ Save setting and make into json file"""
        
        with open(self.setting_file,'w') as cfgfile:
            json.dump(self.setting,cfgfile)
        

#debug per script
if __name__ == "__main__":
    #this code for debug.
    #check app status

    x = cfgInfo.AppStatus
    init = initialize()
    init.implemented_setting()
    s = init.get_setting()
    print(s)
    init.change_setting('name','zy - arps')
    print(s)
    init.save_setting()
    print(cfgInfo.AppName)
    print(x)