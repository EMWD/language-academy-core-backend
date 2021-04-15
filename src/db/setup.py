import psycopg2
from libs.debugger import *


class Setup():

    @staticmethod
    def set_new_conn():
        try:
            conn = psycopg2.connect(database="klime", user="klime",
                                    password="1", host="127.0.0.1", port="5432")

            return conn
            # cursor = conn.cursor()
        except:
            return "Unable to connect database"
