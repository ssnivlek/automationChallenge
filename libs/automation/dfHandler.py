import camelot
import pandas as pd

def pdfToDf(pdf, page):
    dfList = []
    tables = camelot.read_pdf(pdf, pages=f'{page}')

    for table in tables:
        dfList.append(table.df)

    dfRes = pd.concat(dfList)
    dfHeaders = dfRes.iloc[0]
    dfPandas = pd.DataFrame(dfRes.values[1:], columns=dfHeaders)

    return dfPandas

def refactDf(df,date):
    df[['Ingenio','Superficie \nindustrializada','Caña molida','Azúcar blanco \nespecial']]

    df['Data']=''
    df['Data'][0]='Periodo del Report'
    df['Data'][1]=date
    
    return df