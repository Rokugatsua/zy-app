import scr.li_handler as li_handler, scr.db_handler_new as db_handler
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

        ul_db = li_handler.Ul.db('.db')
        li_data = ul_db.li()
        print li_data

        if default_database_name in li_data:
            return True
        else:
            return False

    def initialize_app(self):
        db_handler =''
