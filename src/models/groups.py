from libs.debugger import *
from src.db.setup import Db
from src.helpers.json_formatter import jf

class GroupModel:

    def get_all_groups(self):
        db = Db()
        cursor = db.create_cursor()
        
        try:
            cursor.execute(f"SELECT * FROM groups")
            res = cursor.fetchall()

        except TypeError as e:
            d(e)
        
        db.kill_cursor(cursor)

        res = jf.elems_to_obj(res, ['id', 'group_name', 'group_lang', 'group_level', 'count_of_students', '_action'])
        return res

    def get_group_by_name(self, group_name):
        db = Db()
        cursor = db.create_cursor()

        try:
            cursor.execute(f"""SELECT * FROM groups WHERE group_name = '{str(group_name)}'""")
            res = cursor.fetchall()
        except TypeError as e:
            print(e)

        db.kill_cursor(cursor)

        res = jf.single_elem_to_obj(res, ['id', 'group_name', 'group_lang', 'group_level', 'count_of_students', '_action'])
        return res

    def add_group(self, name, lang, level, numbers, action):
        db = Db()
        cursor = db.create_cursor()

        query = f"INSERT INTO groups (group_name, group_lang, group_level, count_of_students, _action) \
            VALUES ('{name}', '{lang}', '{level}', '{numbers}', '{action}')"
        try:
            cursor.execute(query)
        except TypeError as e:
            print(e)
            return 0
        
        db.kill_cursor(cursor)

        return 1
