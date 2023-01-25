from autoPdfDownload import pdfDownloader
from excelHandler import excelGenerator

def automationMain(path,pages):
    pdfDownloader(path,pages)
    excelGenerator(path)

    return ('Excel File Saved Successfully')

print(automationMain("../../pdfs", ["36","37","38","39","40"]))