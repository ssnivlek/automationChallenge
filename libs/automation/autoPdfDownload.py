import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

def pdfDownloader(path,pages):
    html_page = urlopen("https://www.gob.mx/conadesuca/documentos/dieproc-reportes-de-avance-de-produccion-ciclo-azucarero-2020-2021?state=published")

    soup = BeautifulSoup(html_page) 

    for page in pages:
        for link in soup.select(f'a[href*=Reporte_{page}]'):
            if link.has_attr('href'):
                page2Down=(link['href'])

        pdf = requests.get(page2Down)

        with open(f'{path}/Reporte_{page}.pdf', mode='wb') as file:
            file.write(pdf.content)

        print(f'Pdf Reporte_{page} saved!')