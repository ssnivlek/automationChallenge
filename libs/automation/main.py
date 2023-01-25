from autoPdfHandler import pdfDown
from excelHandler import excelGenerator

def automationMain(path,pages):
    pdfDown(path,pages)
    excelGenerator(path)

    return ('Excel File Saved Successfully')

print(automationMain("../../pdfs", ["36","37","38","39","40"]))