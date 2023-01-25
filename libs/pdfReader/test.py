import re
import pathlib
import camelot
import pandas as pd
from PyPDF2 import PdfReader

def pdfReader(pdf):

    reader = PdfReader(pdf)

    for indexPage, page in enumerate(reader.pages):
        pageText = page.extract_text()

        if re.search(r'([Cc][Uu][Aa][Dd][Rr][Oo][\s\n]7)+',pageText):
            return pageText, indexPage+1, re.search(r'(?<=\s)([0-9]+[A-Za-z\s]+[0-9]+[A-Za-z\s]+[0-9]+)',pageText).group(0)


def pdfToDf(pdf, page):
    dfList = []
    tables = camelot.read_pdf(pdf, pages=f'{page}')

    for table in tables:
        dfList.append(table.df)

    dfRes = pd.concat(dfList)
    dfHeaders = dfRes.iloc[0]
    dfPandas = pd.DataFrame(dfRes.values[1:], columns=dfHeaders)

    return dfPandas

def refacDf(df,date):
    df[['Ingenio','Superficie \nindustrializada','Caña molida','Azúcar blanco \nespecial']]

    df['Data']=''
    df['Data'][0]='Periodo del Report'
    df['Data'][1]=date
    
    return df

def excelGenerator(loc):
    writer = pd.ExcelWriter('reporteFinal.xlsx', engine='xlsxwriter')

    for filePath in pathlib.Path(loc).glob('**/*'):
        strPath = str(filePath)
        result1 = pdfReader(strPath)
        result2 = pdfToDf(strPath,result1[1])
        result3 = refacDf(result2, result1[2])
        result3.to_excel(writer, sheet_name=filePath.stem)

    writer.close()

    return "All Done Excel Generator"

# def main(loc):
#     result1 = pdfReader(loc)
#     result2 = pdfToDf(loc,result1[1])
#     result3 = refacDf(result2, result1[2])
#     print(result3)

excelGenerator('/Users/kelvinsoaresdasilva/Downloads/desafioDO/pdfs')
# main('/Users/kelvinsoaresdasilva/Downloads/desafioDO/pdfs/Reporte_40.pdf')

