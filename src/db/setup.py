import psycopg2
from config import Config
from libs.debugger import *


class Db():

    connection = 0
    config = Config()

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                database=self.config.get_value(['DEV_DB', 'DATABASE']),
                user=self.config.get_value(['DEV_DB', 'USER']),
                password=self.config.get_value(['DEV_DB', 'PASSWORD']),
                host=self.config.get_value(['DEV_DB', 'HOST']),
                port=self.config.get_value(['DEV_DB', 'PORT'])
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