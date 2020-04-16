# Code written by Jerin Rajan on 15th April 2020
# models.py - handles everything that involves a Database.

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.creat_to_do_table()

    def creat_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Description TEXT,
        _is_done boolean,
        _is_deleted boolean,
        CreatedOn Date DEFAULT CURRENT DATE,
        DueDate Date,
        UserID INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
        id INTEGER PRIMARY KEY,
        Name TEXT,
        Email TEXT
        );
        """

        self.conn.execute(query)

class ToDoModel:
    TABLENAME = "TODO"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        
