#this a new dbhandler for match with command pattern.
import abc, sqlite3, os

DATABASE = "default database.db"

class Singleton(type):
    _instance = {}
    def  __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]

class Connection:
    __metaclass__ = Singleton
    def __init__(self,database = DATABASE):
        global DATABASE
        DATABASE = database
        print("init")
        self.conn = None
        try:
            self.conn = sqlite3.connect(DATABASE)
            print("connection to sqlite version " + str(sqlite3.version))
        except sqlite3.Error as e:
            print(e)

    def __call__(self):
        return self.conn

#_____Command_____
class Statement:
    #class object as Comand object
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def statement(self):
        pass

#_____Receiver_____
class enofa_ref:
    # Receiver
    def __init__(self):
        self.tname = "enofa_ref"

    def create(self):
        # the Sql statement 
        s = """
        CREATE TABLE IF NOT EXISTS {}
        (id integer PRIMARY KEY,
        tname text NOT NULL UNIQUE,
        number integer);
        """.format(str(self.tname))
        return s

    def insert(self):
        s = """INSERT INTO {}
        (tname,number) VALUES(?,?)""".format(str(self.tname))
        return s

    def select(self):
        s = """SELECT * FROM {}""".format(str(self.tname))
        return s



#_____Concentre Command____
class Create_The(Statement):
    #concentre Comand
    def __init__(self, func):
        self._func = func

    def statement(self):
        s = self._func.create()
        return s

    def values(self):
        return None

class Insert_To(Statement):
    # concentre command
    def __init__(self, func, values):
        self._func = func
        self._values = values 
    
    def statement(self):
        s = self._func.insert()
        return s

    def values(self):
        return self._values

class Update_Of(Statement):
    # concentre command
    def __init__(self, func, values):
        self._func = func
        self._values = values

    def statement(self):
        s = self._func.update()
        return s

    def values(self):
        return self._values

class Select_from(Statement):
    # concentre command
    def __init__(self, func):
        self._func = func

    def statement(self):
        s = self._func.select()
        return s



# _____Invoker_____
class db:
    # Invoker
    def __init__(self, connection):
        self._connection = connection
        self._cur = self._connection.cursor()
        self._command_list = []

    def set_command(self, command):
        self._command_list.append(command)
        
    def execute(self, statement):
        self._cur.execute(statement)

    def executemany(self, statement, values):
        try:

            self._cur.executemany(statement, values)
        except sqlite3.Error as e:
            print(e)

    def commit(self):
        self._connection.commit()
        print("has save")
    
    def run(self):
        if not self._command_list:
            print("empty command, set first")
        for c in self._command_list:
            statement = c.statement()
            values = c.values()
            if values == None:
                self.execute(statement)
            else:
                self.executemany(statement,values)

        self.commit()

    def get(self, command):
        self._command = command
        self._cur.execute(self._command.statement())
        f  = self._cur.fetchall()
        return f


if __name__ == "__main__":
    conn = Connection()
    print("conn",conn)
    print(conn())
    dbc = db(conn())
    conn_2 = dbc._connection
    print(conn_2)
    
