import random
import string
from src.db.setup import Db
from src.helpers.json_formatter import jf


class LinksModel():

    def add_link(self, link_id, link):
        db = Db()
        cursor = db.create_cursor()

        print(link_id)
        print(link)

        query = f"INSERT INTO links (link_id, link) VALUES ('{link_id}', '{link}')"
        try:
            cursor.execute(query)
        except TypeError as e:
            print(e)
            return 0

        db.kill_cursor(cursor)

        return 1

    def add_links(self, links):
        if len(links) == 0:
            print("LINKS COUNT ERROR")
            return 0

        uniq_link_id = self.create_link_id(8)

        for link in links:
            self.add_link(uniq_link_id, link)

        return uniq_link_id

    def get_all_links(self):
        db = Db()
        cursor = db.create_cursor()

        query = f"SELECT * FROM links"
        try:
            cursor.execute(query)
            res = cursor.fetchall()

        except TypeError as e:
            print(e)
            return 0

        db.kill_cursor(cursor)

        res = jf.elems_to_obj(res, ['id', 'link_id', 'link'])
        return res

    def create_link_id(self, length=8):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


lm = LinksModel()
