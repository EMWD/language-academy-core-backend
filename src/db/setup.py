import psycopg2
from config import Config
from .ip_resolver import ipr
from libs.debugger import *


class Db():

    connection = 0
    config = Config()

    def __init__(self):
        
        current_host = ipr.get_current_config_db_value()
        try:
            self.connection = psycopg2.connect(
                database=self.config.get_value([current_host, 'DATABASE']),
                user=self.config.get_value([current_host, 'USER']),
                password=self.config.get_value([current_host, 'PASSWORD']),
                host=self.config.get_value([current_host, 'HOST']),
                port=self.config.get_value([current_host, 'PORT'])
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

# Export Db instance
# db = Db()
