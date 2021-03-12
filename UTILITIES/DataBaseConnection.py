import mysql.connector
from decouple import config

class MySQLConnection:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=config('MYSQLHost'),
            user=config('MYSQLUser'),
            password=config('MYSQLPassword'),
            database=config('MYSQLDatabase')
        )
        self.cursor = self.mydb.cursor()

    def __del__(self):
        #self.cursor.close()
        self.mydb.close()
