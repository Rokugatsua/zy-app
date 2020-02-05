#import config, sqlite3, os
import sqlite3

database = "database.db"

class Connection:
    def __init__(self):
        try:
            self.conn = sqlite3.connect(database)
        except:
            print("error")

class Create_the:
    def enofa_ref(self):
        pass
    def enofa_list(self):
        pass

class Select_from:
    def enofa_ref():
        pass
    def enofa_list():
        pass

class Insert_to:
    def enofa_ref():
        pass
    def enofa_list():
        pass

class update_of:
    def enofa_ref():
        pass
    def enofa_list():
        pass

if __name__ == "__main__":
    Create_the = Create_the()
    Create_the.enofa_list()
    Create_the.enofa_ref()
    Select_from.enofa_list()
    Select_from.enofa_ref()