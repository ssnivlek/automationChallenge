import re
from PyPDF2 import PdfReader

def pdfSimpleReader(pdf):
    reader = PdfReader(pdf)

    for indexPage, page in enumerate(reader.pages):
        pageText = page.extract_text()

        if re.search(r'([Cc][Uu][Aa][Dd][Rr][Oo][\s\n]7)+',pageText):
            return pageText, indexPage+1, re.search(r'(?<=\s)([0-9]+[A-Za-z\s]+[0-9]+[A-Za-z\s]+[0-9]+)',pageText).group(0)