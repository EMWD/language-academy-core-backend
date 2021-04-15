import psycopg2
from libs.debugger import *
from src.db.setup import Setup

def getSMTH(id):

    cid = f"'{id}'"
    select = f"""SELECT * FROM users WHERE cid = {cid}"""

    conn = Setup.set_new_conn()
    cursor = conn.cursor()
    
    try:
        cursor.execute(select)

        res = cursor.fetchall() 
        for external in res:
            for internal in range(len(external)):
                if internal == 1:
                    print(external[internal]) 

    except TypeError as e:
        print(e)

    cursor.close()
    conn.commit()
    conn.close()

    return res