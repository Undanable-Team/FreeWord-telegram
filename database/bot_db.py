import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS anketa "
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "telegram_id INTEGER UNIQUE,"
               "username VARCHAR (100),"
               "name VARCHAR (100),"
               "age INTEGER,"
               "gender VARCHAR (100),"
               "region TEXT,"
               "photo TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute(
            "INSERT INTO anketa "
            "(telegram_id, username, name, age, gender, region, photo) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            tuple(data.values())
        )
        db.commit()