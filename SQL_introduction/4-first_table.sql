-- create table; shouldn't fail if already exists

CREATE table if not exists first_table (id INT, name VARCHAR(256))
