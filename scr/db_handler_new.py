#this a new dbhandler for match with command pattern.
import abc, sqlite3, os

DATABASE = "database.db"

class Connection:
    def __init__(self):
        try:
            global DATABASE
            DATABASE = DATABASE
            self.conn =  sqlite3.connect("database.db")
            print("conn",self.conn)
        except sqlite3.Error as e:
            print(e)
        self.get_connection()
    def get_connection(self):
        return self.conn
#_____Command_____
class Statement:
    #class object as Comand object
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def statement(self):
        print("has execute")
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
    def __init__(self, conncetion):
        self._connection = conncetion
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
    
    def run(self):
        for c in self._command_list:
            statement = c.statement()
            values = c.values()
            print values
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
    enofaref = enofa_ref()
    values = ["fauna","flora"]
    data = []
    for li in values:
        i = 1
        x = (li,i)
        data.append(x)
    print("data",data)
    create_enofa_ref = Create_The(enofaref)
    insert_enofa_ref = Insert_To(enofaref,data)
    s = insert_enofa_ref.values()
    print(s)

    d = db(Connection().conn)
    d.set_command(create_enofa_ref)
    d.set_command(insert_enofa_ref)
    d.run()

    select_enofa_ref = Select_from(enofaref)
    f = d.get(select_enofa_ref)
    print f

    


