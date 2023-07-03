import os
import ssl
import time
import urllib
import urllib.error
import urllib.request
import requests
from bs4 import BeautifulSoup as bs
from utils import PDFS_PATH, createFolderIfNotExists, download_pdf

# url base
BASE_URL = "https://acervo.fuvest.br/fuvest/"
createFolderIfNotExists(PDFS_PATH)

for ano in range(2010, 2022):
    try:
        # Creates URL and connects to it
        url = BASE_URL + str(ano) + "/"
        context = ssl._create_unverified_context()
        print('Connecting to ' + url + '...')
        response = urllib.request.urlopen(url, context=context)

        # Turns HTML into a soup
        html = response.read().decode()
        soup = bs(html, 'html.parser')

        for anchor in soup.find_all('a'):
            if anchor.string == "Gabarito":
                pdf_url = url + anchor['href']
                break
        
        # Downloads pdf file
        file_name = "gab_" + str(ano) + ".pdf"
        print("Download PDF at " + pdf_url + " ...")
        download_pdf(pdf_url, file_name, PDFS_PATH)

        print("Finished downloading "+ file_name + "!\n")
        
        time.sleep(2)
    except Exception as ex:
        print("An exception of type {} ocurred.".format(type(ex).__name__))