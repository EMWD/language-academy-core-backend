##################################################################
create = """CREATE TABLE users (
        id serial NOT NULL PRIMARY KEY,
        cid varchar NOT NULL
);CREATE TABLE user_pass (
        id serial NOT NULL PRIMARY KEY,
        idc varchar NOT NULL,
        pass varchar NOT NULL
);CREATE TABLE user_data (
        id serial NOT NULL PRIMARY KEY,
        idc varchar NOT NULL,
        first_name varchar NOT NULL,
        last_name varchar NOT NULL
)"""

##################################################################
insert = """INSERT INTO users (cid) VALUES ('BDK1J4')"""

##################################################################
cid = "'first'"
select = f"SELECT * FROM users WHERE cid = {cid}"

cur.execute(select)
res = cur.fetchall() 

for external in res:
    for internal in range(len(external)):
        if internal == 1:
            print(external[internal]) 

##################################################################