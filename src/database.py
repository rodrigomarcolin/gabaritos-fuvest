import sqlite3 as sql
import os,sys
import csv
from utils import CSV_PATH, PARENT_PATH

class Database:
    def __init__(self, name):
        self.con = sql.connect(os.path.join(PARENT_PATH, name))
        self.cur = self.con.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS gabarito (
                id INTEGER NOT NULL PRIMARY KEY,
                questao INTEGER NOT NULL, 
                resposta CHARACTER(1), 
                grupo CHARACTER(1),
                ano INTEGER NOT NULL,
                UNIQUE(questao, grupo, ano)
            )
        """)

        self.op_counter = 0
        self.con.commit()


    def storeQuestion(self, questao, resposta, grupo, ano):
        self.cur.execute("INSERT OR IGNORE INTO gabarito (questao, resposta, grupo, ano) VALUES (?, ?, ?, ?)", (questao, resposta, grupo, ano))
        self.countOp()

    def countOp(self):
        if (self.op_counter % 50 == 0):
            self.op_counter = 0
            self.con.commit()
        else:
            self.op_counter += 1
        
        return

    def __del__(self):
        self.con.commit()
        self.cur.close()