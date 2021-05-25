import psycopg2
import random
import string
from libs.debugger import *
from src.db.setup import Db

class UsersModel:

    def get_all_users(self):
        db = Db()
        cursor = db.create_cursor()

        query1 = f"SELECT * FROM users"
        query2 = f"SELECT * FROM user_data"
        query3 = f"SELECT * FROM user_pass"
    
        try:
            cursor.execute(query2)
            res = cursor.fetchall()

        except TypeError as e:
            d(e)
        
        db.kill_cursor(cursor)

        return res

    def get_user(self, id):
        db = Db()
        cursor = db.create_cursor()

        id = str(id)
        query = f"""SELECT * FROM user_data WHERE uid = '{id}'"""
        try:
            cursor.execute(query)
            res = cursor.fetchall()

            print("RES")
            print(res)

        except TypeError as e:
            d(e)
        
        db.kill_cursor(cursor)

        return res

    def add_user(self, name, last_name, password):
        db = Db()
        cursor = db.create_cursor()
        
        test_uid = self.get_random_string(6)

        query1 = f"INSERT INTO users (uid) VALUES ('{test_uid}')"
        query2 = f"INSERT INTO user_data (uid, name, last_name) VALUES ('{test_uid}', '{str(name)}', '{str(last_name)}')"
        query3 = f"INSERT INTO user_pass (uid, pass) VALUES ('{test_uid}', {str(password)})"
        
        try:
            cursor.execute(query1)
            cursor.execute(query2)
            cursor.execute(query3)
        except TypeError as e:
            d(e)
            return 0
        
        db.kill_cursor(cursor)

        return 1

    def get_random_string(self, length):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(length))