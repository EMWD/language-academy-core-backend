-- remove previous tables
;
DROP SCHEMA public CASCADE;
CREATE SCHEMA public; 
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;

-- create all tables

-- users part
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

-- groups part
CREATE TABLE GROUPS(
   ID  SERIAL PRIMARY KEY,
   GROUP_NAME           TEXT      NULL,
   GROUP_LANG           TEXT      NULL,
   GROUP_LEVEL           TEXT     NULL,
   COUNT_OF_STUDENTS           TEXT         NULL,
   _ACTION           TEXT      NULL
);
