import psycopg2
from libs.debugger import *
from src.db.setup import Db

class UsersModel:

    def get_all_users(self):
        db = Db()
        cursor = db.create_cursor()

        query = f"SELECT * FROM users"
        try:
            cursor.execute(query)
            res = cursor.fetchall()

        except TypeError as e:
            d(e)
        
        db.kill_cursor(cursor)

        return res

    def get_user(self, id):
        db = Db()
        cursor = db.create_cursor()

        id = str(id)
        query = f"""SELECT * FROM users WHERE cid = '{id}'"""
        try:
            cursor.execute(query)
            res = cursor.fetchall()

            print("RES")
            print(res)

        except TypeError as e:
            d(e)
        
        db.kill_cursor(cursor)

        return res

    def add_user(seld, name, last_name, password):
        db = Db()
        cursor = db.create_cursor()
        
        query1 = f"INSERT INTO users (uid) VALUES ('TEST_UID')"
        query2 = f"INSERT INTO user_data (uid, name, last_name) VALUES ('TEST_UID', '{str(name)}', '{str(last_name)}')"
        query3 = f"INSERT INTO user_pass (uid, pass) VALUES ('TEST_UID', {str(password)})"
        
        try:
            cursor.execute(query1)
            cursor.execute(query2)
            cursor.execute(query3)
        except TypeError as e:
            d(e)
            return 0
        
        db.kill_cursor(cursor)

        return 1