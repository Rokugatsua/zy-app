import os


# This config the application

class cfgDir:
    BaseDir = os.getcwd()
    UIDir =  os.path.join(BaseDir, "UI")
    ScrDir = os.path.join(BaseDir, "scr")
    DbDir = os.path.join(BaseDir, "db")
    FileDir = os.path.join(BaseDir, "_file")

class cfgInfo:
    AppName = "Zy App"
    AppVersion = "Version 00.0001"
    sts = {"Under Development":"ud","Big Bug":"bb","Stable":"s"}
    AppStatus = sts["Under Development"]
    


#debug per script
if __name__ == "__main__":
    #this code for debug.
    #check app status
    x = cfgInfo.AppStatus
    print(x)