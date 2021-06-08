from libs.debugger import *
from src.helpers.json_formatter import jf


class AuthModel:

    def __init__(self, Db):
        self.db = Db()

    def try_auth(self, email):
        return self.is_user_exist(email)

    def is_user_exist(self, email):
        cursor = self.db.create_cursor()
        query = f"""SELECT * FROM user_data WHERE email = '{str(email)}'"""

        try:
            cursor.execute(query)
            res = cursor.fetchall()
        except TypeError as e:
            d(e)

        self.db.kill_cursor(cursor)

        if res:
            return 1
        return 0
