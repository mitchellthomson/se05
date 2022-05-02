import sqlite3

CREATE_FLAVOR_TABLE = "CREATE TABLE FLAVORS (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER"
def connection():
    sqlite3.connect("data.db")

def create_tables():
    with connection:
        connection.execute(CREATE_FLAVOR_TABLE)
    