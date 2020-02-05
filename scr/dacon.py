import scr.li_handler as li_handler
import config
import os

class Out:
    class list:
        def __init__(self):
            pass
        def csv(self):
            ul_csv = li_handler.Ul.file('.csv')
            li = ul_csv.li()
            return li

class In:
    pass
    

class OnReady:
    def check_init(self):
        # Check initialize or basic configure for this app
        default_database_name = 'database.db'
        for root, dic, files in os.walk(config.cfgDir.DbDir):
            print(files)
            if default_database_name in files:
                print(files)
                return True
            else:
                return False