from sqlite3 import connect


def connect_db():
    db = connect('Saloon.sqlite3')
    return db

