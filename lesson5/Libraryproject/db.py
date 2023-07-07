import sqlite3

class DB:
    con = sqlite3.connect("library_db.sqlite")
    cur = con.cursor()

    query_table1 = """
    create table if not exists users(
        id integer primary key autoincrement,
        name varchar(40),
        usernme varchar (40) not null unique ,
        password varchar(20) not null,
        role varchar (20) not null default 'USER',
        create_at date default current date
    )"""
    query_table2 = """
        create table if not exists categorys(
            id integer primary key autoincrement,
            name varchar(40) not null,
            create_at date default current date
        )
        """
    query_table3 = """
        create table if not exists books(
            id integer primary key autoincrement,
            name varchar(40) not null,
            category_id integer,
            caounte integer not null default 1,
            create_at date default current date
            )
            """
    query_table4 = """
        create table if not exists books_users(
            id integer primary key autoincrement,
            user_id integer,
            book_id integer,
            status integer default 1,
            create_at timestamp default current_timestamp
            )
            """

    cur.execute(query_table1)
    cur.execute(query_table2)
    cur.execute(query_table3)
    cur.execute(query_table4)
    con.commit()