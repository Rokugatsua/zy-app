import scr.li_handler as li_handler, scr.db_handler_new as db_handler, scr.file_handler as file_handler
import config
import os

class Out:
    class to_db:
        def __init__(self):
            db_dir_file = os.path.join(config.cfgDir.DbDir, config.cfgInfo.DATABASE)
            set_database = db_handler.Connection(db_dir_file)
            db = db_handler.db(set_database())
            self.db = db

        def get_enofa_ref(self):
            enofa_ref = db_handler.enofa_ref()
            select_enofa_ref =  db_handler.Select_from(enofa_ref)
            data = self.db.get(select_enofa_ref)
            new_data = [list(rows) for rows in data]
            return new_data

        def get_enofa_list(self, tname):
            enofa_list = db_handler.enofa_list(tname)
            select_enofa_list = db_handler.Select_from(enofa_list)
            data = self.db.get(select_enofa_list)
            new_data = [list(rows) for rows in data]
            return new_data

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

    class to_db:
        def __init__(self):
            db_dir_file = os.path.join(config.cfgDir.DbDir, config.cfgInfo.DATABASE)
            set_database = db_handler.Connection(db_dir_file)
            db = db_handler.db(set_database())
            self.db = db
        
        def save_enofa_list(self, csv_name):
            #get enofa in csv file
            csv_dir_file = os.path.join(config.cfgDir.FileDir,"csv",csv_name)
            efaktur_export = file_handler.Efaktur_Export(csv_dir_file)
            datali = efaktur_export.get()

            # sclicing or gruping data with enofa refrence
            O = Out.to_db()
            enofaref = O.get_enofa_ref()
            dacon = {}
            for ref_li in enofaref:
                tname = str(ref_li[1])
                ref = str(ref_li[2])
                awal = int(ref_li[3])
                akhir = int(ref_li[4])
                dacon[tname] = []
                for li in datali:
                    nofp = int(li[-8:])
                    if li.startswith(ref) and awal <= nofp <= akhir:
                        dacon[tname].append(nofp)

            #send to db
            # making values 
            has_record = 1 #alternative boolean values True
            values = []
            new_dacon = {}
            for tname in dacon:
                new_dacon[tname] = []
                for li in dacon[tname]:
                    val = (has_record,li)
                    new_dacon[tname].append(val)
            

            #save to table in db
            for tname in new_dacon:
                data = new_dacon[tname]
                if data:
                    enofa_list =  db_handler.enofa_list(tname)
                    update_enofa_list = db_handler.Update_Of(enofa_list,data)
                    self.db.set_command(update_enofa_list)
                    self.db.run()


        def save_enofa_ref(self, enofa_awal, enofa_akhir):
            enofas = enofa_awal
            enofae = enofa_akhir
            refs = enofas[:5]
            refe = enofae[:5]
            datali = []
            if refs == refe:
                tname = "enofa" + enofas + "to" + enofa_akhir
                label = enofas + " - " + enofae
                awal = int(enofas[-8:])
                akhir =  int(enofae[-8:]) + 1
                datali = [i for i in range(awal,akhir)]

                values = (str(tname), str(refs), str(awal), str(akhir), str(label))

            has_record = 0 
            valueli = []
            for li in datali:
                val = (int(li),int(has_record))
                valueli.append(val)                

            enofa_ref = db_handler.enofa_ref()
            enofa_list =  db_handler.enofa_list(tname)

            in_enofa_ref = db_handler.Insert_To(enofa_ref,values)
            cr_enofa_list = db_handler.Create_The(enofa_list)
            in_enofa_list = db_handler.Insert_To(enofa_list,valueli)

            self.db.set_command(in_enofa_ref)
            self.db.set_command(cr_enofa_list)
            self.db.set_command(in_enofa_list)

            self.db.run()

    

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
