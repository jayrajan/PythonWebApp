# Code written by Jerin Rajan on 15th April 2020
# models.py - handles everything that involves a Database.
import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Description TEXT,
        _is_done boolean,
        _is_deleted boolean,
        CreatedOn TEXT,
        DueDate TEXT,
        UserID INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)

    def create_user_table(self):
        # query = """
        # CREATE TABLE IF NOT EXISTS "User" (
        # id INTEGER PRIMARY KEY,
        # Name TEXT,
        # Email TEXT
        # );
        # """
        # self.conn.execute(query)
        pass

class ToDoModel:
    TABLENAME = "Todo"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        # self.TABLENAME = "TODO"

    def create(self, text, description):
        query = f'insert into {self.TABLENAME} ' \
                f'(Title, Description) ' \
                f'values ("{text}","{description}")'
        result = self.conn.execute(query)
        return result

    def list_items(self, where_clause=""):
        query = f"SELECT id, Title, Description, DueDate, _is_done " \
                f"from {self.TABLENAME} WHERE _is_deleted != {1} " + where_clause
        print (query)
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result
