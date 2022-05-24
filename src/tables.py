import os
import camelot
from utils import CSV_PATH, PDFS_PATH, createFolderIfNotExists

createFolderIfNotExists(CSV_PATH)

for ano in range(2010, 2023):
    try:
        pdf_name = 'gab_' + str(ano) + '.pdf'
        tables_path = os.path.join(CSV_PATH, str(ano))
        createFolderIfNotExists(tables_path)
        tables = camelot.read_pdf(os.path.join(PDFS_PATH, pdf_name))
        print("Tables Extracted from {}: {}".format(pdf_name, tables.n))

        for i in range(len(tables)):
            csv_name = 'gab_' + str(ano) + '_' + str(i) + '.csv'
            tables[i].to_csv(os.path.join(tables_path, csv_name))
    except Exception as ex:
        print("An exception of type {} has ocurred.".format(type(ex).__name__))