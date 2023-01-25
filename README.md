## Automation Challenge

**Objective:** Create libs to read .pdf and automation of .xlsx file creation

**Automation steps:**

- Download pdfs of "Report_36~40" from the following website:
  https://www.gob.mx/conadesuca/documentos/dieproc-reportes-de-avance-de-produccion-ciclo-azucarero-2020-2021?state=published
- After reading the .pdf and transforming the "Cuadro 7" table into a dataframe
- Delete columns from the dataframe and add a new one with the Reporting period
- Transform the dataframes of all the Reports into a single .xlsx file with each dataframe being an excel sheet.

Third-party libs used:\_ \*\* \*\*
Other libs listed in requirements.txt

- Camelot
- PyPDF2
- BeautifulSoup
- Requests
- GhostScript
- OpenCV
- XlsxWriter

**How to run the application:**
_After installing all the necessary libs via requirements.txt_, follow these steps:
Run the `main.py` file in the `libs/automation` folder:

    python3 main.py
    or
    python main.py

The file itself has an example of the parameters expected to run the application, use them to get a brief idea\_

Any other questions please contact me ;)
