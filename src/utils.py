import os, requests
import csv

PARENT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
CSV_PATH = os.path.join(PARENT_PATH, 'csvs')
PDFS_PATH = os.path.join(PARENT_PATH, 'pdfs')
DB_PATH = os.path.join(PARENT_PATH)
VALID_ANSWERS=['A', 'B', 'C', 'D', 'E']
def createFolderIfNotExists(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print("Created " + path + '/')

def download_pdf(url, name, path):        
    r = requests.get(url, stream=True)
    file_name = os.path.join(path, name)
    with open(file_name, 'wb') as file_dest:
        file_dest.write(r.content)

def parse2010(path, db):
    print("Storing 2010...")
    ano = 2010
    reader = csv.reader(open(path))
    header = [i.split('\n')[-1] for i in next(reader)]
    size = len(header)

    for row in reader:
        resp = row[0]
        for i in range(1, size):
            questao = row[i]
            grupo = header[i]
            db.storeQuestion(questao, resp, grupo, ano)

def parseOld(path, ano, db):
    ano = int(ano)
    reader = csv.reader(open(path))
    grupo = next(reader)[0].split()[-1]
    print("Storing {} {}...".format(ano, grupo))
    for row in reader:
        for entry in row:
            entry = entry.replace('\xa0', ' ')
            entry = entry.replace('-','‐').split('‐')
            questao = entry[0].split()[-1]
            resposta = entry[-1].strip()
            if resposta.upper() not in VALID_ANSWERS:
                resposta = 'X'

            db.storeQuestion(questao, resposta, grupo, ano)

def parseRecent(path, ano, db):
    ano = int(ano)
    reader = csv.reader(open(path))
    grupo = next(reader)[0].split()[-1]
    print("Storing {} {}...".format(ano, grupo))
    for row in reader:
        questao, resp = row[:2]
        if resp.upper() not in VALID_ANSWERS:
                resp = 'X'
        db.storeQuestion(questao, resp, grupo, ano)

        questao, resp = row[3:]
        if resp.upper() not in VALID_ANSWERS:
                resp = 'X'
        db.storeQuestion(questao, resp, grupo, ano) 