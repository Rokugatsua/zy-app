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

        def db(self):
            ul_db = li_handler.Ul.db('.db')
            li = ul_db.li()
            return li

class In:
    class setting:
        def new_db(self, name_db, ondefault = bool):
            O_li = Out.list()
            li_db = O_li.db()
            _onready = OnReady()
            if name_db in li_db:
                print(name_db + " has exists")
            else:
                if ondefault:
                    cfg = config.initialize()
                    cfg.change_setting("database",name_db)
                    cfg.save_setting()
                    config.cfgInfo.DATABASE = name_db
                    _onready.initialize_app()
                    pass
                else:
                    config.cfgInfo.DATABASE = name_db
                    _onready.initialize_app()


            pass

    

class OnReady:
    def check_init(self):
        # Check initialize or basic configure for this app
        default_database_name = config.cfgInfo.DATABASE

        ul_db = li_handler.Ul.db('.db')
        li_data = ul_db.li()

        if default_database_name in li_data:
            return True
        else:
            return False

    def initialize_app(self):
        # initialize the database 
        db_dir_file = os.path.join(config.cfgDir.DbDir, config.cfgInfo.DATABASE)
        set_database =  db_handler.Connection(db_dir_file)
        db = db_handler.db(set_database()) # call set_database() being to get sqlite.connection()
        enofa_ref = db_handler.enofa_ref()
        create_enofa_ref = db_handler.Create_The(enofa_ref)
        db.set_command(create_enofa_ref)
        db.run()
