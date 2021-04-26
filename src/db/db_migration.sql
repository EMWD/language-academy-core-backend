-- remove previous tables
;
DROP SCHEMA public CASCADE;
CREATE SCHEMA public; 
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;

-- create all tables
CREATE TABLE USERS(
   ID  SERIAL PRIMARY KEY,
   UID        CHAR(8)
);
CREATE TABLE USER_DATA(
   ID  SERIAL PRIMARY KEY,
   UID        CHAR(8),
   NAME           TEXT      NOT NULL,
   LAST_NAME           TEXT      NOT NULL
);
CREATE TABLE USER_PASS(
   ID  SERIAL PRIMARY KEY,
   UID        CHAR(8),
   PASS           CHAR(50)      NOT NULL
);
