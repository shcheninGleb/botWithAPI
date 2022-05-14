import sqlite3


dbName = 'data.db'


def initDb():
    sqlite_connection = sqlite3.connect(dbName)
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS tokens (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL);'''

    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()


def addToken(symbol):
    sqlite_connection = sqlite3.connect(dbName)
    cursor = sqlite_connection.cursor()
    query = """INSERT INTO tokens(name)  VALUES  ('{}')""".format(symbol)
    print(query)
    cursor.execute(query)
    sqlite_connection.commit()


def getTokens():
    sqlite_connection = sqlite3.connect(dbName)
    cursor = sqlite_connection.cursor()
    query = """SELECT name from tokens"""
    cursor.execute(query)
    rows = cursor.fetchall()
    return list(map(lambda x: x[0], rows))
