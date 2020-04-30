#imports

import sqlite3 as sqlite
import pandas as pd
import csv
import json

class dbdump:
    def __init__ (self, path):
        self.con = sqlite.connect(path)
        self.metadata = {}

    def __close__ (self):
        self.con.close()

    def createdump(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
        tables = cursor.fetchall()
        for table in tables:
            table_name = table[0]
            cursor.execute("SELECT * FROM %s" % table_name)
            data = [description[0] for description in cursor.description]
            data_dict = [{data}]
