import psycopg2
from libs.debugger import *
from src.db.setup import Db

class GroupModel:

    def get_all_groups(self):

        db = Db()
        cursor = db.create_cursor()

        query1 = f"SELECT * FROM groups"

        try:
            cursor.execute(query1)
            res = cursor.fetchall()

        except TypeError as e:
            d(e)
        
        db.kill_cursor(cursor)

        return res

    def add_group(self, name, lang, level, numbers, action):
        db = Db()
        cursor = db.create_cursor()

        query2 = f"INSERT INTO groups (group_name, group_lang, group_level, count_of_students, _action) VALUES ('Group1', 'English', '1', '3', 'asas')"
        # query2 = f"INSERT INTO groups (group_name, group_lang, group_level, count_of_students, _action) VALUES ('{name}', '{lang}', '{level}')"
        
        try:
            cursor.execute(query2)
        except TypeError as e:
            d(e)
            return 0
        
        db.kill_cursor(cursor)

        return 1
