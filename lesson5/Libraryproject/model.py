from dataclasses import dataclass

from lesson5.Libraryproject.db import DB

@dataclass
class User(DB):
    id : int = None
    name : str = None
    username : str = None
    password : str = None
    role : str = None
    created_at : str = None

    def check_username(self):
        query = """select id from users where username = ?"""
        parametr = (self.username,)
        self.cur.execute(query , parametr)
        if self.cur.fetchone():
            return True

    def save_user(self):# noqa
        query = """insert into users(name,username,password)
        values(? , ? , ?)"""
        parametr = (self.name , self.username , self.password)# noqa
        self.cur.execute(query , parametr)
        self.con.commit()

    def login_check(self):
        query = """select id from users where username = ? and password = ?"""
        parametr = (self.username, self.password)
        user_id = self.cur.fetchone()
        if user_id:
            return user_id

@dataclass
class Book(DB):
    id: int = None
    name: str = None
    cagtegory_id: int = None
    count : int = None
    created_at: str = None

@dataclass
class BookUsers(DB):
    id: int = None
    user_id: int = None
    book_id: int = None
    status: int = None
    created_at: str = None