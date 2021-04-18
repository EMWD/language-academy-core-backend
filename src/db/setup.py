import psycopg2
from config import Config
from libs.debugger import *


class Db():

    connection = 0
    config = Config()

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                database = self.config.get_value(['DEV_DB', 'database']), 
                user = self.config.get_value(['DEV_DB', 'user']),
                password = self.config.get_value(['DEV_DB', 'password']), 
                host = self.config.get_value(['DEV_DB', 'host']),  
                port = self.config.get_value(['DEV_DB', 'port'])
                )
        except:
            return "Unable to connect database"

    def create_cursor(self):
        return self.connection.cursor()

    def kill_connect(self):
        self.connection.commit()
        self.connection.close()

    def kill_cursor(self, cursor):
        cursor.close()
        self.kill_connect()