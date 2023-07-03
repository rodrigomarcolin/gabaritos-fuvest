from utils import parse2010, parseRecent, parseOld
from utils import CSV_PATH
from database import Database
import os

# Inicializando banco de dados
db = Database('data.db')

# Esse código me dá dor de cabeça
for folder in os.listdir(CSV_PATH):
    ano = int(folder)
    for file in os.listdir(os.path.join(CSV_PATH, folder)):
        file_path = os.path.join(CSV_PATH, folder, file)
        if ano == 2010:
            parse2010(file_path, db)
        elif ano >= 2020:
            parseRecent(file_path, ano, db)
        else:
            parseOld(file_path, ano, db)
