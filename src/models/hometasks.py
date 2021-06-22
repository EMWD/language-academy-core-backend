from libs.debugger import *
from src.db.setup import Db
from src.helpers.json_formatter import jf
from .links import lm


class HometaskModel:

    def get_all_hometasks(self):
        db = Db()
        cursor = db.create_cursor()

        query1 = f"SELECT * FROM hometasks"
        try:
            cursor.execute(query1)
            res = cursor.fetchall()
        except TypeError as e:
            d(e)

        db.kill_cursor(cursor)

        res = jf.elems_to_obj(
            res, ['id', 'task_description', 'task_name', 'due_date', 'links_id', 'action'])
        return res

    def add_hometask(self, description, name, duedate, link, action):
        db = Db()
        cursor = db.create_cursor()

        uniq_links_id = lm.add_links(['NONE_1', 'NONE_2'])

        insert_query = f"INSERT INTO hometasks (task_description, task_name, due_date, links_id, _action) VALUES \
            ('{description}', '{name}', '{duedate}', '{uniq_links_id}', '{action}')"
        try:
            cursor.execute(insert_query)
        except TypeError as e:
            d(e)
            return 0

        db.kill_cursor(cursor)

        return 1
