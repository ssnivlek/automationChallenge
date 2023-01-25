import importlib.machinery
import pandas as pd
import pathlib
from dfHandler import pdfToDf, refactDf

pdfLibLoader = importlib.machinery.SourceFileLoader('pdfHandler', '../../libs/pdfReader/pdfHandler.py')
pdfHandler = pdfLibLoader.load_module('pdfHandler')

def excelGenerator(loc):
    writer = pd.ExcelWriter('../../xlsx/reporteFinal.xlsx', engine='xlsxwriter')

    for filePath in pathlib.Path(loc).glob('**/*'):
        strPath = str(filePath)

        resultReader = pdfHandler.pdfSimpleReader(strPath)
        resultPdfDf = pdfToDf(strPath,resultReader[1])
        resultDf = refactDf(resultPdfDf, resultReader[2])
        resultDf.to_excel(writer, sheet_name=filePath.stem)

    writer.close()

    print("Excel File Generated")