import sqlite3
import os
import uuid
import datetime
from dotenv import load_dotenv, dotenv_values

load_dotenv()


class DBHandler:
    def __init__(self):
        try:
            self.conn = sqlite3.connect(os.getenv("DATABASE"))
        except sqlite3.Error as e:
            print("[dbHandler][init]" + str(e))
        self.check_tables()

    def check_tables(self):
        tables = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        if tables.rowcount != 0:
            for table in tables.fetchall():
                print(table[0])
        else:
            print("No tables")
            #TODO Create missing tables


    def save_pickup(self, data, hash):
        cursor = self.conn.cursor()
        sql = "INSERT INTO pickups (id, timeRequested, data, hash) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (str(uuid.uuid4()), datetime.datetime.now(), data, hash))
        self.conn.commit()
        cursor.close()


    def shutdown(self):
        self.conn.close()