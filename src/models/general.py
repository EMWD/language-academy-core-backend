import psycopg2
from libs.debugger import *
from src.db.setup import Db


def getSMTH(id):

    cid = f"'{id}'"
    select = f"""SELECT * FROM users WHERE cid = {cid}"""

    db = Db()
    cursor = db.create_cursor()

    try:
        cursor.execute(select)

        res = cursor.fetchall()
        for external in res:
            for internal in range(len(external)):
                if internal == 1:
                    print(external[internal])

    except TypeError as e:
        d(e)

    db.kill_cursor(cursor)

    return res
